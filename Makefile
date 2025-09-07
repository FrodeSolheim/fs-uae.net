all: templates public_html

public_html:
	mkdir -p public_html
	python3 make.py

scrape:
	scripts/scrape.sh
	scripts/remove-empty-pages.py

templates:
	rm -Rf templates/scraped
	mkdir -p templates/scraped
	python3 scripts/create-templates-from-scraped.py

.PHONY: public_html scrape templates
