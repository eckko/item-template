# Item template

The smallest possible repo for one book. It holds only the book's own files
and the workflows; all the quiz and reader code (screens, themes, spaced
repetition, sync, build tools) is loaded from a tagged copy of
[`eckko/item-ui`](https://github.com/eckko/item-ui) on jsDelivr. Book repos
are made from it by the **Create book** action in
[`eckko/actions`](https://github.com/eckko/actions) (private repo, topic
`book`) and kept in step by its **Update book** action.

## What is in it

| Path | What it is |
|---|---|
| `index.html` | A tiny loader: shows the favicon, reads `item-version` and loads the quiz from item-ui on the CDN |
| `item-version` | One line: the item-ui version to load (`3` or `3.1.0`) |
| `questions.json` | The question bank. A **sample**; replace it |
| `images/favicon.png` | The browser-tab icon |
| `media/` | The book's pictures, encrypted (`media/<id>.enc`) |
| `references/` | The book's EPUB and PDF and your notes (never published as they are) |
| `.github/workflows/publish-to-subject.yml` | Builds the encrypted reader and quiz and publishes them into a subject site made from `group-template` |
| `.github/workflows/auto-pr.yml` | Opens a pull request when a branch is first pushed |
| `tools/set_item_version.py` | Writes `item-version` |

## Choose the item UI version

`item-version` is one line. `3` follows the newest `3.x.x` release; `3.1.0`
is exactly that release and never changes. The publish workflow turns a major
into the newest exact tag before it builds. Release actions of item-ui may
update this file in new releases.

## Publish

The workflow needs the secrets `SUBJECT_REPO_TOKEN` (a token for the subject
repo only, Contents: read and write) and `SUBJECT_KEY` (the subject key), and
the variable `SUBJECT_REPO` (the subject repo's name). Create book sets all
three. It runs on a push to `main` that changes `references/`,
`questions.json`, `media/`, `book-structure/` or `item-version`, or by hand:

```
gh workflow run publish-to-subject.yml -f SUBJECT_REPO=habit -f TEMPLATE_TAG=3.4.0
```

The plain book never leaves this repo: the job reads the EPUB (and your notes
EPUB) and `questions.json`, encrypts everything with the subject key inside
the runner and publishes only encrypted files, under names that say nothing
about the book (see `ai-context/opaque-site.md` in item-ui).
