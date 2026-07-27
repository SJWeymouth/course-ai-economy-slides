# The AI Economy — Summer 2026 slides

Quarto/Reveal.js source files for the course slide decks.

## Local workflow

1. Clone this repository to your computer.
2. Open `course-ai-economy-slides.Rproj` in RStudio.
3. Open a `.qmd` file and click **Render** to preview the deck locally.
4. Commit and push changes to `main`.

## Shared assets

All slide decks draw from the single root-level `assets/` folder. Keep the larger master image archive in Dropbox and copy only files actually used by the course into `assets/`.

Reference shared files from a deck with a project-root path, for example:

```markdown
![](/assets/filename.png)
```

## GitHub Pages publishing

The workflow at `.github/workflows/publish.yml` automatically installs Quarto and R, renders the site into `_site`, and deploys it to GitHub Pages whenever `main` changes.

After the workflow file is present:

1. Open the repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to **GitHub Actions**.
4. Open the **Actions** tab and watch the `Publish Quarto slides` workflow.
5. When it succeeds, the site will be available at:

`https://sjweymouth.github.io/course-ai-economy-slides/`

## Adding a new deck

Create a new `.qmd` file under `slides/dayN/`, render it locally, and add a link to `index.qmd`. The PDFs can be exported separately and posted to the university course system.
