# fs-uae.net

This repository contains the code and templates needed to generated the [FS-UAE](https://fs-uae.net) website. Right now, it mostly contains a dump (scraped) of the old wordpress site to make a static site independent of Wordpress and databases.

Later, this repository will evolve with new/improved content, and I expect the scraped content to be gradually replaced.

Directories:

- `public_html` - Contains some static content and is the target directory for the built site.
- `_scraped` - Contains a scraped copy of the old fs-uae.net wordpress site as of 2025-09-06.
- `templates/scraped` - Contains jinja2 templates based on the scraped pages (header and footer) are extracted to common templates (etc).

You need Python 3 and Jinja 2 in order to build the `public_html` directory. Just run `python3 _scripts/make.py`.
