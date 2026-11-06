This repo is the shell for one book: `index.html` (a loader), `.itemrc`,
`questions.json`, `images/`, `media/`, `references/` and the workflows. All
quiz and reader code is loaded from a tagged copy of
https://github.com/eckko/item-ui on jsDelivr. Do not add `css/`, `js/`,
`htrab/`, `themes/` or `vendor/` here.
The version is the one line in `.itemrc` (a major like `3`, or an exact
one like `3.1.0`; `python3 tools/set_item_version.py VERSION`). Never use a
branch. The release action of item-ui may update `.itemrc` in this
repo. Book repos made from this one get new actions through the pipeline
(eckko/actions, "Update book"), which copies every file except the book's own
data (`references/`, `questions.json`, `media/`, `images/`, `book-structure/`,
`.itemrc`). For the code, tools, tests and AI notes (AGENTS.md,
ai-context/), see the item-ui repo.
