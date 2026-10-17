#!/usr/bin/env python3
"""Check what `zensical build --strict` cannot see.

  scripts/check-docs.py              # every check; exit 1 if any fails

--strict fails a broken internal link or anchor, but not a nav entry that names
a missing page. It says nothing about a page that no nav names, a locale that
has drifted from the other, an llms.txt index that has lost a page, the lists of
repositories disagreeing, a link from a player's docs into this site that lands
on no page or on an anchor no heading names with an explicit id, or a Japanese
line break the browser renders as a space. This script checks those.

scripts/build-docs.sh and build-docs.ps1 run it before building, so CI and a
publish run it too. It needs only the standard library, so any Python 3 on PATH
can run it.

Each check prints what it compared. A check that cannot run says "skipped" and
why -- the deep-link and inbound-link checks need the sibling repositories
cloned next to this one, and CI has none -- so read the output, not just the
exit code.
"""

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


def locale_pages(locale):
    base = os.path.join(ROOT, "docs", locale)
    pages = set()
    for d, _, files in os.walk(base):
        for name in files:
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


SIBLING_REF = re.compile(r"github\.com/cri-middleware/([A-Za-z0-9_.-]+)/(blob|tree)/([^/\s)>\"'`]+)/([^\s)>\"'`#]*)")


def sibling_links():
    links = []
    for path in tracked("*.md", "*.yml", "*.html"):
        for i, line in enumerate(read(path).split("\n"), 1):
            for m in SIBLING_REF.finditer(line):
                links.append((path, i) + m.groups())
    return links


def check_head_links(links):
    problems = [f"{p}:{i}: {repo}/{kind}/{ref}/ -- write {kind}/HEAD/, not a branch"
                for p, i, repo, kind, ref, _ in links if ref != "HEAD"]
    report("links use HEAD", problems, f"{len(links)} links into repositories go through blob/HEAD or tree/HEAD")


def check_deep_links(links):
    siblings = os.path.dirname(ROOT)
    problems, resolved, missing_clone = [], 0, {}
    for p, i, repo, _, ref, sub in links:
        if ref != "HEAD":
            continue
        clone = ROOT if repo == "SpriteStudio-Docs" else os.path.join(siblings, repo)
        if clone != ROOT and not os.path.exists(os.path.join(clone, ".git")):
            missing_clone[repo] = missing_clone.get(repo, 0) + 1
            continue
        if os.path.exists(os.path.join(clone, sub.rstrip("/"))):
            resolved += 1
        else:
            problems.append(f"{p}:{i}: {repo} has no {sub} in the clone at {clone}")
    if not resolved and not problems:
        skipped("deep links", f"no sibling repository is cloned next to this one ({siblings})")
        return
    report("deep links", problems,
           f"{resolved} paths exist in the local clones' working trees, which may not be on the default branch")
    for repo, n in sorted(missing_clone.items()):
        skipped("deep links", f"{n} into {repo}: no clone at {os.path.join(siblings, repo)}")


PORTAL_LINK = re.compile(r"cri-middleware\.github\.io/SpriteStudio-Docs/([^\s)>\"'`#]*)(?:#([^\s)>\"'`]+))?")
EXPLICIT_ID = re.compile(r"^#{1,6} .*\{[^}]*#([^\s}]+)[^}]*\}\s*$")


def check_inbound_links():
    """What the sibling repositories link to on this site: a page, and an anchor a heading names.

    The anchor has to be an explicit id (`{ #id }`) on the heading, so rewording the
    heading leaves the link where it was. Links to files the build makes (llms.txt)
    are not pages and are left out.
    """
    siblings = os.path.dirname(ROOT)
    problems, links, anchors, clones = [], 0, 0, 0
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
                    loc, page = ("ja", where[3:]) if where == "ja" or where.startswith("ja/") else ("en", where)
                    if "." in page.rsplit("/", 1)[-1]:
                        continue
                    links += 1
                    pages = [f"docs/{loc}/{page}.md", f"docs/{loc}/{page}/index.md"] if page else [f"docs/{loc}/index.md"]
                    md = next((c for c in pages if os.path.isfile(os.path.join(ROOT, c))), None)
                    if not md:
                        problems.append(f"{repo}/{path}:{i}: links {m.group(0)}, but there is no {pages[0]}")
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
           f"{links} links from {clones} sibling clones land on a page, and the {anchors} with an anchor "
           f"on a heading's explicit id")


# Chrome renders a soft line break as a space, also between two Japanese
# characters and next to Japanese punctuation, where the pages write none. Beside
# a link they do write one, so a break there is that space.
JA = re.compile(r"[　-〿぀-ヿ㐀-䶿一-鿿！-･]")
JA_PUNCT = re.compile(r"[　-〿！-／：-＠［-｀｛-･]")
BLOCK_START = re.compile(r"^([-*+] |\d+\. |\||#|!!!|\?\?\?|>|```|<)")
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
            if a.strip().startswith("```"):
                fence = not fence
            if "<!--" in a:
                comment = "-->" not in a.split("<!--", 1)[1]
            elif "-->" in a:
                comment = False
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
    check_structure()
    check_repositories()
    links = sibling_links()
    check_head_links(links)
    check_deep_links(links)
    check_inbound_links()
    check_japanese_breaks()
    print(f"{APP}: {'FAILED -- ' + str(failures) + ' check(s)' if failures else 'done'}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
