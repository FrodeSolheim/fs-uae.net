all: templates public_html

public_html:
	mkdir -p public_html
	python3 _scripts/build.py

scrape:
	_scripts/scrape.sh
	_scripts/remove-empty-pages.py

templates:
	rm -Rf _templates/scraped
	mkdir -p _templates/scraped
	python3 _scripts/create-templates-from-scraped.py

.PHONY: public_html scrape templates
