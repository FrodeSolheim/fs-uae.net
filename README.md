# fs-uae.net

This repository contains the code and templates needed to generated the [FS-UAE](https://fs-uae.net) website. Right now, it mostly contains a dump (scraped) of the old wordpress site to make a static site independent of Wordpress and databases.

Later, this repository will evolve with new/improved content, and I expect the scraped content to be gradually replaced.

## Documentation

The `docs` directory contains documentation for FS-UAE 3. Updates should be submitted to the fs-uae repo (fs-uae-3 branch) instead, and updates will be synced over here. Maybe later the docs will be pulled automatically from the fs-uae repo, but this is how it works for now.

## Building

You need jekyll and some plugins in order to build the site. Use bundler to install the dependencies from Gemfile with `bundle install`.

To develop the site with automatic rebuilds:
```
bundle exec jekyll serve
```

To build a static version in `_dist`:
```
bundle exec jekyll build
```

## Other directories

- `_scraped` - Contains a scraped copy of the old fs-uae.net wordpress site as of 2025-09-06.
- `templates/scraped` - Contains jinja2 templates based on the scraped pages (header and footer) are extracted to common templates (etc).
