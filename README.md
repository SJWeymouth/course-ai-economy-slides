# The AI Economy

Source repository for the University of Basel course website and Quarto/Reveal.js slide decks:

https://sjweymouth.github.io/course-ai-economy-slides/

The deployed website is a single page with three sections:

- **Syllabus** — a stable link to the PDF published automatically from the private course repository
- **Slides** — links maintained manually in `index.qmd`
- **Activities** — links generated automatically from the private course repository

## Slide workflow

1. Pull the latest `main` branch.
2. Open `course-ai-economy-slides.Rproj` in RStudio.
3. Edit or create a deck under `slides/dayN/`.
4. Render the `.qmd` file locally to check the deck.
5. Add or update its link under **Slides** in `index.qmd`.
6. Commit and push the source, assets, and `index.qmd` changes to `main`.

A deck can be successfully deployed at its direct URL without appearing on the homepage. It appears under **Slides** only after its link is added to `index.qmd`.

## Shared slide assets

All decks use the root-level `assets/` folder. Keep the larger master image archive in Dropbox and copy only the files used by the course into this repository.

Reference a shared asset from a deck with a project-root path:

```markdown
![](/assets/filename.png)
```

The scripts in `scripts/` copy selected Dropbox assets into the repository when needed.

## Syllabus and activity publishing

Do not edit the syllabus PDF, activity PDFs, or `activities/list.qmd` in this repository. They are generated from LaTeX sources in the private `SJWeymouth/course-ai-economy-2026` repository.

The automated path is:

**Overleaf → `course-ai-economy-2026` → compiled syllabus and public activity PDFs → this repository → course website**

The course workflow publishes `syllabus/AI_Economy_2026_Syllabus.tex` as `syllabus/AI_Economy_2026_Syllabus.pdf`. It also publishes student-facing PDFs from `activities/core/` and `activities/simulations/`, commits them to `activities/`, and regenerates `activities/list.qmd`. The homepage links to the stable syllabus path and includes the generated activity list.

## GitHub Pages deployment

The workflow at `.github/workflows/publish.yml` renders the Quarto project into `_site` and deploys it to GitHub Pages whenever `main` changes.

After a push:

1. Open the repository's **Actions** tab.
2. Watch **Publish Quarto slides**.
3. Allow about 1–3 minutes for the build and deployment; occasionally it may take longer.
4. If the workflow is green but the browser still shows the old page, force-refresh with **Ctrl+F5**.

Do not commit generated `_site/` files.
