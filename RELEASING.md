# Publishing SpriteStudio-Docs

Maintainers only. Building the site to check your own edits is in
[CONTRIBUTING.md](./CONTRIBUTING.md); this is the published tree and the deploy.

```bash
scripts/build-pages.sh serve=yes    # both locales, served on :8000
```

`build-pages.sh` is the whole published site: `build-docs.sh` run for you, then a static server
over `site/`. That server is the point of it, and the one thing `zensical serve` cannot do — both
locales at once, so the header's language selector resolves. `pages.yml`'s build job **is** this
script with every option spelled out, so a publish cannot change because a default did, and CI
and the local gate cannot drift.

**Deployment is manual.** `pages.yml` runs on `workflow_dispatch` alone: merging to `main`
publishes nothing. So `scripts/*` are production tooling — keep them mode `100755` and working
with no options.

<br>

---

# SpriteStudio-Docs の公開手順

維持者向けです。自分の編集を確認するためのビルドは [CONTRIBUTING.md](./CONTRIBUTING.md) にあります。
ここでは公開ツリーとデプロイを扱います。

```bash
scripts/build-pages.sh serve=yes    # 両ロケールを :8000 で配信
```

`build-pages.sh` が公開サイト全体です。`build-docs.sh` を実行したうえで `site/` を静的配信します。
この配信こそがこのスクリプトの目的で、`zensical serve` にできない唯一のこと — 両ロケールを同時に
出して、ヘッダーの言語セレクタを解決させること — です。`pages.yml` のビルドジョブは**このスクリプト**
（オプションはすべて明示）なので、既定値の変更で公開内容が変わることがなく、CI と手元のゲートも
ずれません。

**デプロイは手動です。** `pages.yml` は `workflow_dispatch` だけで動き、`main` へのマージでは
何も公開されません。したがって `scripts/*` は本番ツールです。モード `100755` を保ち、オプション
無しで動く状態を維持してください。
