#!/usr/bin/env python3
"""Check what `zensical build --strict` cannot see.

  scripts/check-docs.py              # every check; exit 1 if any fails

--strict fails a broken internal link or anchor, but not a nav entry that names
a missing page. It says nothing about a page that no nav names, a locale that
has drifted from the other, an llms.txt index that has lost a page, the lists of
repositories disagreeing, a redirect that differs between locales or ends on no
page, a link into a repository that names a branch (outside a code block, where a
command may need one) or a path its clone does not have, a link from a sibling's
docs into this site that lands on neither a page nor a redirect to one (or on an
anchor no heading names with an explicit id), a link from the agent plugin that
lands on no page, a link from this site to a page or demo a sibling's site does
not build, or a Japanese line break the browser renders as a space.
This script checks those.

scripts/build-docs.sh and build-docs.ps1 run it before building, so CI and a
publish run it too. It needs only the standard library, so any Python 3 on PATH
can run it.

Each check prints what it compared. A check that cannot run says "skipped" and
why -- the deep-link, inbound-link and outbound-link checks need the sibling
repositories cloned next to this one, and CI has none -- so read the output,
not just the exit code.
"""

import json
import os
import re
import subprocess
import sys
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP = os.path.basename(__file__)
LOCALES = {"en": "mkdocs.yml", "ja": "mkdocs.ja.yml"}
SDK = "SpriteStudio-SDK"

failures = 0


def report(name, problems, summary):
    global failures
    if problems:
        failures += 1
        print(f"{APP}: {name:<22} FAILED")
        for p in problems:
            print(f"    {p}")
    else:
        print(f"{APP}: {name:<22} ok       {summary}")


def skipped(name, why):
    print(f"{APP}: {name:<22} skipped  {why}")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def tracked(*patterns):
    """Files git does not ignore that match the pathspecs, or a walk when this is not a checkout.

    Untracked files count, so a page not yet added is checked; deleted ones do not.
    """
    try:
        out = subprocess.check_output(
            ["git", "-C", ROOT, "ls-files", "--cached", "--others", "--exclude-standard", "--", *patterns],
            stderr=subprocess.DEVNULL,
        )
        listed = set(out.decode("utf-8").split("\n")[:-1])
        return sorted(p for p in listed if os.path.isfile(os.path.join(ROOT, p)))
    except (OSError, subprocess.CalledProcessError):
        exts = tuple(p.rsplit(".", 1)[-1] for p in patterns)
        found = []
        for d, dirs, files in os.walk(ROOT):
            dirs[:] = [x for x in dirs if x not in (".git", ".venv", "site", ".cache")]
            for name in files:
                if name.endswith(exts):
                    found.append(os.path.relpath(os.path.join(d, name), ROOT).replace(os.sep, "/"))
        return sorted(found)


_paths = {}


def paths_in(clone):
    """Every file and directory git has in a clone, spelled as git spells it.

    Asked of git rather than the disk: a case-insensitive disk finds a path written
    with the wrong case, and the disk finds untracked files, and GitHub and Pages
    serve neither. This repository's own untracked pages count, as in tracked(), and
    so does a walk of it when it is not a checkout; a sibling's git failing is fatal.
    """
    if clone not in _paths:
        cmd = ["git", "-C", clone, "ls-files", "-z", "--cached"]
        if clone == ROOT:
            cmd += ["--others", "--exclude-standard"]
        try:
            listed = subprocess.check_output(cmd, stderr=subprocess.PIPE).decode("utf-8").split("\0")[:-1]
            files = {f for f in listed if os.path.lexists(os.path.join(clone, f))}
        except (OSError, subprocess.CalledProcessError) as e:
            if clone != ROOT:
                sys.exit(f"{APP}: cannot list the files git has in {clone}: {getattr(e, 'stderr', b'').decode().strip() or e}")
            files = set()
            for d, dirs, names in os.walk(clone):
                dirs[:] = [x for x in dirs if x not in (".git", ".venv", "site", ".cache")]
                files |= {os.path.relpath(os.path.join(d, n), clone).replace(os.sep, "/") for n in names}
        found = set(files)
        for f in files:
            parts = f.split("/")[:-1]
            found |= {"/".join(parts[:k]) for k in range(1, len(parts) + 1)}
        _paths[clone] = found
    return _paths[clone]


def locale_pages(locale):
    base = os.path.join(ROOT, "docs", locale)
    pages = set()
    for d, _, files in os.walk(base):
        for name in files:
            # Finder leaves a .DS_Store in whichever locale's folder it opened.
            if not name.startswith("."):
                pages.add(os.path.relpath(os.path.join(d, name), base).replace(os.sep, "/"))
    return pages


# --- config parsing ---------------------------------------------------------
# The configs carry `!!python/...` tags that a plain YAML loader rejects, and the
# two sequences read here have one fixed shape, so they are read line by line.
# A parse that finds nothing fails the check rather than passing it.

def top_level_block(text, key):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line == f"{key}:":
            block = []
            for nxt in lines[i + 1:]:
                if nxt and not nxt.startswith((" ", "#")):
                    break
                block.append(nxt)
            return block
    return []


NAV_ITEM = re.compile(r"^( *)- (.+?):(?: (\S+\.md))?$")


def nav_tree(config):
    """[(depth, path-or-None)] in order; None marks a section."""
    tree = []
    for line in top_level_block(read(config), "nav"):
        m = NAV_ITEM.match(line.rstrip())
        if m:
            tree.append((len(m.group(1)) // 2, m.group(3)))
    return tree


def llmstxt_pages(config):
    """(section names, page paths in order) from plugins > llmstxt > sections."""
    sections, pages, inside = [], [], None
    for line in top_level_block(read(config), "plugins"):
        stripped = line.strip()
        if stripped == "sections:":
            inside = len(line) - len(line.lstrip())
            continue
        if inside is None or not stripped:
            continue
        if len(line) - len(line.lstrip()) <= inside:
            break
        m = re.match(r"^- (\S+\.md):", stripped)
        if m:
            pages.append(m.group(1))
        elif stripped.endswith(":"):
            sections.append(stripped[:-1])
    return sections, pages


def redirect_maps(config):
    """{source page: target page} from plugins > redirects > redirect_maps."""
    maps, inside = {}, None
    for line in top_level_block(read(config), "plugins"):
        stripped = line.strip()
        if stripped == "redirect_maps:":
            inside = len(line) - len(line.lstrip())
            continue
        if inside is None or not stripped:
            continue
        if len(line) - len(line.lstrip()) <= inside:
            break
        m = re.match(r"^(\S+\.md): (\S+\.md)$", stripped)
        if m:
            maps[m.group(1)] = m.group(2)
    return maps


# --- checks -----------------------------------------------------------------

def check_locale_files():
    en, ja = locale_pages("en"), locale_pages("ja")
    problems = [f"docs/en/{p} has no docs/ja/{p}" for p in sorted(en - ja)]
    problems += [f"docs/ja/{p} has no docs/en/{p}" for p in sorted(ja - en)]
    report("locale files", problems, f"{len(en)} files, the same in docs/en and docs/ja")


def check_nav():
    trees = {loc: nav_tree(cfg) for loc, cfg in LOCALES.items()}
    problems = [f"{LOCALES[loc]}: no nav entries found" for loc, t in trees.items() if not t]
    if not problems and trees["en"] != trees["ja"]:
        for i, (a, b) in enumerate(zip(trees["en"], trees["ja"])):
            if a != b:
                problems.append(f"entry {i + 1} differs: {a} in mkdocs.yml, {b} in mkdocs.ja.yml")
                break
        else:
            problems.append(f"{len(trees['en'])} entries in mkdocs.yml, {len(trees['ja'])} in mkdocs.ja.yml")
    pages = [p for _, p in trees["en"] if p]
    report("nav", problems,
           f"{len(pages)} pages, {len(trees['en']) - len(pages)} sections, the same structure in both configs")
    return {loc: [p for _, p in t if p] for loc, t in trees.items()}


def check_pages_in_nav(nav):
    problems = []
    for loc, cfg in LOCALES.items():
        on_disk = {p for p in locale_pages(loc) if p.endswith(".md")}
        named = set(nav[loc])
        problems += [f"docs/{loc}/{p} is in no nav entry of {cfg}" for p in sorted(on_disk - named)]
        problems += [f"{cfg} names {p}, which docs/{loc}/ does not have" for p in sorted(named - on_disk)]
    report("pages in nav", problems, "every page in docs/<locale> is named by that locale's nav")


def check_llmstxt(nav):
    problems, counts = [], {}
    for loc, cfg in LOCALES.items():
        sections, pages = llmstxt_pages(cfg)
        counts[loc] = len(sections)
        if not pages:
            problems.append(f"{cfg}: no llmstxt sections found")
        elif pages != nav[loc]:
            missing = [p for p in nav[loc] if p not in pages]
            extra = [p for p in pages if p not in nav[loc]]
            if missing or extra:
                problems += [f"{cfg}: {p} is in nav but not in llmstxt.sections" for p in missing]
                problems += [f"{cfg}: {p} is in llmstxt.sections but not in nav" for p in extra]
            else:
                problems.append(f"{cfg}: llmstxt.sections lists the pages in a different order from nav")
    if counts["en"] != counts["ja"]:
        problems.append(f"{counts['en']} llmstxt sections in mkdocs.yml, {counts['ja']} in mkdocs.ja.yml")
    report("llms.txt sections", problems,
           f"each config's llmstxt.sections lists its nav's pages in nav order ({counts['en']} sections)")


def check_redirects():
    """Each redirect ends on a page of its locale, leaves from a page that is gone, and both locales have the same."""
    problems, maps = [], {loc: redirect_maps(cfg) for loc, cfg in LOCALES.items()}
    if maps["en"] != maps["ja"]:
        problems.append(f"redirect_maps differ: {maps['en']} in mkdocs.yml, {maps['ja']} in mkdocs.ja.yml")
    for loc, cfg in LOCALES.items():
        for source, target in maps[loc].items():
            if not os.path.exists(os.path.join(ROOT, "docs", loc, target)):
                problems.append(f"{cfg}: {source} redirects to docs/{loc}/{target}, which does not exist")
            if os.path.exists(os.path.join(ROOT, "docs", loc, source)):
                problems.append(f"{cfg}: {source} redirects, but docs/{loc}/{source} is still a page")
    report("redirects", problems,
           f"{len(maps['en'])} redirect{'s' * (len(maps['en']) != 1)}, the same in both configs, each from a page that is gone to one that exists")


def redirected(where):
    """The page a redirect sends a URL path of this site to, or None."""
    loc, page = ("ja", where[3:]) if where == "ja" or where.startswith("ja/") else ("en", where)
    maps = redirect_maps(LOCALES[loc])
    target = next((maps[s] for s in (f"{page}.md", f"{page}/index.md") if s in maps), None)
    return f"docs/{loc}/{target}" if target and f"docs/{loc}/{target}" in paths_in(ROOT) else None


def structure(text):
    counts = {"headings": 0, "table rows": 0, "code fences": 0, "admonitions": 0}
    fence = False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("```"):
            counts["code fences"] += 1
            fence = not fence
        elif fence:
            continue
        elif s.startswith("#"):
            counts["headings"] += 1
        elif s.startswith("|"):
            counts["table rows"] += 1
        elif s.startswith(("!!!", "???")):
            counts["admonitions"] += 1
    return counts


def check_structure():
    problems, n = [], 0
    pages = sorted(p for p in locale_pages("en") & locale_pages("ja") if p.endswith(".md"))
    for p in pages:
        en, ja = structure(read(f"docs/en/{p}")), structure(read(f"docs/ja/{p}"))
        n += 1
        for k in en:
            if en[k] != ja[k]:
                problems.append(f"{p}: {en[k]} {k} in en, {ja[k]} in ja")
    report("page structure", problems,
           f"{n} pages with the same headings, table rows, code fences and admonitions in en and ja")


REPO_LINK = re.compile(r"github\.com/cri-middleware/([A-Za-z0-9_.-]+)")


def repos_in(path):
    return set(REPO_LINK.findall(read(path))) - {"SpriteStudio-Docs"}


def check_repositories():
    problems, total = [], 0
    for loc in LOCALES:
        lists = {f: repos_in(f"docs/{loc}/{f}") for f in ("index.md", "license.md", "support.md")}
        cards = lists["index.md"]
        total = len(cards)
        for f, repos in lists.items():
            for r in sorted(cards - repos):
                problems.append(f"docs/{loc}/{f} does not link {r}, which index.md has a card for")
            for r in sorted(repos - cards):
                problems.append(f"docs/{loc}/{f} links {r}, which index.md has no card for")
        with_page = set()
        for p in locale_pages(loc):
            if p.startswith("players/") and p.endswith(".md"):
                with_page |= repos_in(f"docs/{loc}/{p}")
        for r in sorted(cards - {SDK} - with_page):
            problems.append(f"docs/{loc}/players/ has no page linking {r}")
    report("repositories", problems,
           f"index.md, license.md and support.md list the same {total} repositories, "
           f"and each but the SDK has a players/ page (en, ja)")


SIBLING_REF = re.compile(r"github\.com/cri-middleware/([A-Za-z0-9_.-]+)/(blob|tree)/([^/\s)>\"'`#]+)(?:/([^\s)>\"'`#]*))?")


FENCE = re.compile(r"^\s*(?:>\s?)*```")


def sibling_links():
    """Links into the repositories, each marked whether it sits in a fenced code block.

    A URL in a code block is a command's argument, not a link a reader follows, so it
    spells whatever ref the command's tool accepts.
    """
    links = []
    for path in tracked("*.md", "*.yml", "*.html"):
        fenced = False
        for i, line in enumerate(read(path).split("\n"), 1):
            if path.endswith(".md") and FENCE.match(line):
                fenced = not fenced
                continue
            for m in SIBLING_REF.finditer(line):
                links.append((path, i, fenced) + m.groups(""))
    return links


def check_head_links(links):
    problems = [f"{p}:{i}: {repo}/{kind}/{ref}/ -- write {kind}/HEAD/, not a branch"
                for p, i, fenced, repo, kind, ref, _ in links if ref != "HEAD" and not fenced]
    commands = sum(1 for _, _, fenced, _, _, ref, _ in links if fenced and ref != "HEAD")
    report("links use HEAD", problems,
           f"{len(links) - commands} links into repositories go through blob/HEAD or tree/HEAD, "
           f"and {commands} in code blocks name the branch a command needs")


def check_deep_links(links):
    siblings = os.path.dirname(ROOT)
    problems, resolved, own, missing_clone = [], 0, 0, {}
    for p, i, fenced, repo, _, ref, sub in links:
        if ref != "HEAD" and not fenced:
            continue
        clone = ROOT if repo == "SpriteStudio-Docs" else os.path.join(siblings, repo)
        if clone != ROOT and not os.path.exists(os.path.join(clone, ".git")):
            missing_clone[repo] = missing_clone.get(repo, 0) + 1
            continue
        if not sub.strip("/") or sub.strip("/") in paths_in(clone):
            if clone == ROOT:
                own += 1
            else:
                resolved += 1
        else:
            problems.append(f"{p}:{i}: {repo} has no {sub} in git in the clone at {clone}")
    if not resolved and not problems:
        mine = f"; links into this repository resolve ({own})" if own else ""
        skipped("deep links", f"no sibling repository is cloned next to this one ({siblings}){mine}")
        return
    report("deep links", problems,
           f"{resolved + own} paths are in git, as spelled, in the local clones, "
           f"which may not be on the default branch")
    for repo, n in sorted(missing_clone.items()):
        skipped("deep links", f"{n} into {repo}: no clone at {os.path.join(siblings, repo)}")


PORTAL_LINK = re.compile(r"cri-middleware\.github\.io/SpriteStudio-Docs/([^\s)>\"'`#]*)(?:#([^\s)>\"'`]+))?")
EXPLICIT_ID = re.compile(r"^#{1,6} .*\{[^}]*#([^\s}]+)[^}]*\}\s*$")


def portal_page(where):
    """The Markdown file behind a page of this site, or None, and the file it would most likely be."""
    loc, page = ("ja", where[3:]) if where == "ja" or where.startswith("ja/") else ("en", where)
    pages = [f"docs/{loc}/{page}.md", f"docs/{loc}/{page}/index.md"] if page else [f"docs/{loc}/index.md"]
    return next((c for c in pages if c in paths_in(ROOT)), None), pages[0]


def check_inbound_links():
    """What the sibling repositories link to on this site: a page, and an anchor a heading names.

    The anchor has to be an explicit id (`{ #id }`) on the heading, so rewording the
    heading leaves the link where it was. A link to a page that moved lands through
    its redirect, and the summary counts those. Links to files the build makes
    (llms.txt) are not pages and are left out.
    """
    siblings = os.path.dirname(ROOT)
    problems, links, anchors, clones, moved = [], 0, 0, 0, 0
    for repo in sorted(repos_in("docs/en/index.md")):
        clone = os.path.join(siblings, repo)
        if not os.path.exists(os.path.join(clone, ".git")):
            continue
        clones += 1
        out = subprocess.check_output(["git", "-C", clone, "ls-files", "--", "*.md"], stderr=subprocess.DEVNULL)
        for path in out.decode("utf-8").split("\n")[:-1]:
            with open(os.path.join(clone, path), encoding="utf-8") as f:
                lines = f.read().split("\n")
            for i, line in enumerate(lines, 1):
                for m in PORTAL_LINK.finditer(line):
                    where, anchor = m.group(1).strip("/"), m.group(2)
                    if "." in where.rsplit("/", 1)[-1]:
                        continue
                    links += 1
                    md, likely = portal_page(where)
                    if not md:
                        md = redirected(where)
                        moved += bool(md)
                    if not md:
                        problems.append(f"{repo}/{path}:{i}: links {m.group(0)}, but there is no {likely}")
                        continue
                    if anchor:
                        anchors += 1
                        anchor = urllib.parse.unquote(anchor)
                        ids = {x.group(1) for x in map(EXPLICIT_ID.match, read(md).split("\n")) if x}
                        if anchor not in ids:
                            problems.append(f"{repo}/{path}:{i}: links #{anchor} on {md}, which no heading names "
                                            f"with an explicit {{ #{anchor} }}")
    if not clones:
        skipped("inbound links", f"no sibling repository is cloned next to this one ({siblings})")
        return
    report("inbound links", problems,
           f"{links} links from {clones} sibling clones land on a page ({moved} through a redirect), "
           f"and the {anchors} with an anchor on a heading's explicit id")


def check_plugin_links():
    """What the agent plugin links to on this site: a page the site builds.

    An installed copy of the plugin is not rebuilt with the site, so a page it names
    has to keep existing. Links to files the build makes (llms.txt) are left out,
    and anchors are not checked.
    """
    problems, links = [], 0
    files = [p for p in tracked("plugins/*.md") if p.startswith("plugins/")]
    for path in files:
        for i, line in enumerate(read(path).split("\n"), 1):
            for m in PORTAL_LINK.finditer(line):
                where = m.group(1).strip("/")
                if "." in where.rsplit("/", 1)[-1]:
                    continue
                links += 1
                md, likely = portal_page(where)
                if not md:
                    problems.append(f"{path}:{i}: links {m.group(0)}, but there is no {likely}")
    report("plugin links", problems, f"{links} links from {len(files)} plugin files land on a page of this site")


SIBLING_SITE_LINK = re.compile(r"cri-middleware\.github\.io/([A-Za-z0-9_.-]+)/([^\s)>\"'`#]*)")


def sibling_site_has(clone, where):
    loc, page = ("ja", where[3:]) if where == "ja" or where.startswith("ja/") else ("en", where)
    roots = [f"docs/{loc}"] + (["docs"] if loc == "en" else [])
    candidates = [f"{r}/{page}.md" for r in roots if page]
    candidates += [f"{r}/{page}/index.md" if page else f"{r}/index.md" for r in roots]
    if not page:
        candidates.append("libs/ssruntime/docs/README.ja.md" if loc == "ja" else "libs/ssruntime/docs/README.md")
    files = paths_in(clone)
    if any(c in files for c in candidates):
        return True
    if where == "ssconverter" or where.startswith("ssconverter/"):
        versions = "packages/ssconverter-web/versions.json"
        if versions not in files:
            return False
        with open(os.path.join(clone, versions), encoding="utf-8") as f:
            schemas = {v["schema"] for v in json.load(f)["versions"]}
        return where == "ssconverter" or where.split("/", 1)[1] in schemas
    if not where or "scripts/build-pages.sh" not in files:
        return False
    with open(os.path.join(clone, "scripts", "build-pages.sh"), encoding="utf-8") as f:
        code = "\n".join(l for l in f.read().split("\n") if not l.lstrip().startswith("#"))
    return re.search(rf"(?:\bsite|\$\{{?OUT\}}?)/{re.escape(where)}(?![\w.-])", code) is not None


def check_outbound_links():
    """What this site links to on the sibling repositories' sites: a page or a demo they build.

    A page is a Markdown file in the sibling's docs; a demo is a path its
    scripts/build-pages.sh writes under site/ or $OUT, or a converter schema in its
    versions.json. Links to files (llms.txt) are left out, and anchors are not checked.
    """
    siblings = os.path.dirname(ROOT)
    problems, resolved, missing_clone = [], 0, {}
    for path in tracked("*.md", "*.yml", "*.html"):
        for i, line in enumerate(read(path).split("\n"), 1):
            for m in SIBLING_SITE_LINK.finditer(line):
                repo, where = m.group(1), m.group(2).strip("/")
                if repo == "SpriteStudio-Docs" or "." in where.rsplit("/", 1)[-1]:
                    continue
                clone = os.path.join(siblings, repo)
                if not os.path.exists(os.path.join(clone, ".git")):
                    missing_clone[repo] = missing_clone.get(repo, 0) + 1
                    continue
                if sibling_site_has(clone, where):
                    resolved += 1
                else:
                    problems.append(f"{path}:{i}: links {m.group(0)}, which {repo} at {clone} does not build")
    if not resolved and not problems:
        skipped("outbound links", f"no sibling repository is cloned next to this one ({siblings})")
        return
    report("outbound links", problems,
           f"{resolved} links to sibling sites match a page or demo in git, as spelled, in the local clones, "
           f"which may not be on the default branch")
    for repo, n in sorted(missing_clone.items()):
        skipped("outbound links", f"{n} into {repo}: no clone at {os.path.join(siblings, repo)}")


# Chrome renders a soft line break as a space, also between two Japanese
# characters and next to Japanese punctuation, where the pages write none. Beside
# a link they do write one, so a break there is that space.
JA = re.compile(r"[　-〿぀-ヿ㐀-䶿一-鿿！-･]")
JA_PUNCT = re.compile(r"[　-〿！-／：-＠［-｀｛-･]")
BLOCK_START = re.compile(r"^([-*+] |\d+\. |\||#|!!!|\?\?\?|>|```|<)")
QUOTE = re.compile(r"^\s*(?:>\s?)+")
LINK_START = re.compile(r"^[*_]*\[")
LINK_END = re.compile(r"\]\([^()\s]*\)$")


def rendered_end(line):
    """The last character a reader sees on this line, past emphasis and a link's URL."""
    s = line.rstrip()
    m = LINK_END.search(s)
    if m:
        s = s[:m.start()]
    s = s.rstrip("*_]")
    return s[-1:] if s else ""


def rendered_start(line):
    s = line.strip().lstrip("*_[")
    return s[:1]


def check_japanese_breaks():
    problems, files = [], tracked("*.md")
    for path in files:
        lines = read(path).split("\n")
        fence = comment = False
        for i in range(len(lines) - 1):
            a, b = lines[i], lines[i + 1]
            qa, qb = QUOTE.match(a), QUOTE.match(b)
            if a[qa.end():].strip().startswith("```") if qa else a.strip().startswith("```"):
                fence = not fence
            if "<!--" in a:
                comment = "-->" not in a.split("<!--", 1)[1]
            elif "-->" in a:
                comment = False
            if qa and qb:
                if qa.group().count(">") != qb.group().count(">"):
                    continue
                a, b = a[qa.end():], b[qb.end():]
            if fence or comment or not a.strip() or not b.strip():
                continue
            if a.strip().startswith(("#", "|", "!!!", "???")) or BLOCK_START.match(b.strip()):
                continue
            x, y = rendered_end(a), rendered_start(b)
            if not x or not y:
                continue
            if JA_PUNCT.match(x) or JA_PUNCT.match(y):
                why = "next to Japanese punctuation"
            elif LINK_END.search(a.rstrip().rstrip("*_")) or LINK_START.match(b.strip()):
                continue
            elif JA.match(x) and JA.match(y):
                why = "between two Japanese characters"
            elif (JA.match(x) and y == "&") or (x == "&" and JA.match(y)):
                why = "inside a word joined by &"
            else:
                continue
            problems.append(f"{path}:{i + 1}: line break {why} renders as a space: "
                            f"...{a.rstrip()[-12:]!r} / {b.strip()[:12]!r}...")
    report("Japanese line breaks", problems, f"{len(files)} Markdown files break lines only where a space belongs")


def main(argv):
    # A console without UTF-8 would otherwise crash on the Japanese in a report, hiding it.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(errors="backslashreplace")
    if any(a in ("-h", "--help", "help") for a in argv):
        print(__doc__.strip())
        return 0
    if argv:
        print(f"{APP}: takes no arguments (see {APP} --help)", file=sys.stderr)
        return 2
    check_locale_files()
    nav = check_nav()
    check_pages_in_nav(nav)
    check_llmstxt(nav)
    check_redirects()
    check_structure()
    check_repositories()
    links = sibling_links()
    check_head_links(links)
    check_deep_links(links)
    check_inbound_links()
    check_plugin_links()
    check_outbound_links()
    check_japanese_breaks()
    print(f"{APP}: {'FAILED -- ' + str(failures) + ' check(s)' if failures else 'done'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
