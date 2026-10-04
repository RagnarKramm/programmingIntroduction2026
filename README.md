# Markdown docs on GitHub Pages

A small Jekyll documentation site with automatic sidebar navigation, responsive styling, and dark mode. GitHub builds it; no local installation is required.

## Publish

1. Create a GitHub repository (use a public repository for the simplest setup), or open your existing repository.
2. Upload the `docs` folder from this starter into the repository root. The resulting path should be `docs/_config.yml`, not `github-pages-docs/docs/_config.yml`.
3. Commit the files to `main`.
4. Open **Settings → Pages**.
5. Under **Build and deployment**, choose **Deploy from a branch**.
6. Select **main** and **/docs**, then click **Save**.
7. Wait for the Pages deployment to finish. Settings → Pages will show the published link, usually `https://USERNAME.github.io/REPOSITORY/`.

## Customize

- Edit `docs/_config.yml` to change the site title and description.
- Edit `docs/index.md` for your home page.
- Add Markdown files with front matter containing `title` and `nav_order`. Follow `docs/getting-started.md`.
- Leave out `nav_order` to hide a page from the sidebar while keeping its URL available.
- Use the `relative_url` filter for links and images; GitHub Pages supplies the repository base path.
- Do not add `.nojekyll`: this site needs Jekyll to convert Markdown to HTML.

## Verification

The starter has not been built locally. After publishing, confirm the Pages deployment succeeds, open the home page, and check the Getting started link and sidebar. Deployment details are available in the repository's Actions tab.

Official setup reference: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
