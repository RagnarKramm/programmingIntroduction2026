---
title: Getting started
nav_order: 2
---

# Getting started

## Add a page

Create `docs/my-guide.md` with this content:

```markdown
---
title: My guide
nav_order: 3
---

# My guide

Write your documentation here.
```

The title appears in the sidebar. The `nav_order` number controls its position.

## Link to another page

Use the `relative_url` filter so links work under your repository's URL:

{% raw %}
```liquid
[My guide]({{ '/my-guide.html' | relative_url }})
```
{% endraw %}

## Add images

Put images in `docs/assets/`, then reference them like this:

{% raw %}
```liquid
![Screenshot]({{ '/assets/screenshot.png' | relative_url }})
```
{% endraw %}

## Publish updates

Commit your edits to the `main` branch. GitHub Pages rebuilds the site automatically.
