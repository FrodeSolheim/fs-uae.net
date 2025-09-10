# fs-uae.net

This repository contains the code and templates needed to generated the [FS-UAE](https://fs-uae.net) website. Right now, it mostly contains a dump (scraped) of the old wordpress site to make a static site independent of Wordpress and databases.

Later, this repository will evolve with new/improved content, and I expect the scraped content to be gradually replaced.

You need jekyll in order to build the site.

To build a static version in `_dist`:
```
bundle exec jekyll build
```

To develop the site with automatic rebuilds:
```
bundle exec jekyll serve
```

Directories:

- `_scraped` - Contains a scraped copy of the old fs-uae.net wordpress site as of 2025-09-06.
- `templates/scraped` - Contains jinja2 templates based on the scraped pages (header and footer) are extracted to common templates (etc).
