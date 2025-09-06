#!/bin/sh

# set -e

mkdir -p scrape
cd scrape

# SCRAPE="wget --mirror -nH --trust-server-names -X files,wp-json -e robots=off"
SCRAPE="wget --recursive -nH --trust-server-names -X files,wp-json -e robots=off"

# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=1"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=2"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=3"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=4"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=5"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=6"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=7"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=8"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=9"
# $SCRAPE "https://wordpress.fs-uae.net/wp-json/wp/v2/pages?per_page=100&page=10"

# jq -r '.[].link' \
# wp-json/wp/v2/'pages?per_page=100&page=1' \
# wp-json/wp/v2/'pages?per_page=100&page=2' \
# wp-json/wp/v2/'pages?per_page=100&page=3' \
# wp-json/wp/v2/'pages?per_page=100&page=4' \
# wp-json/wp/v2/'pages?per_page=100&page=5' \
# wp-json/wp/v2/'pages?per_page=100&page=6' \
# wp-json/wp/v2/'pages?per_page=100&page=7' \
# wp-json/wp/v2/'pages?per_page=100&page=8' \
# wp-json/wp/v2/'pages?per_page=100&page=9' \
# wp-json/wp/v2/'pages?per_page=100&page=10' \
# > links.txt

# cat links.txt | $SCRAPE -i -

$SCRAPE https://wordpress.fs-uae.net/links.html

# --convert-links

echo "Scraping done, removing some files..."

echo "Removing some files..."

rm -f "robots.txt"
rm -rf "wp-admin"
rm -f "wp-login.php"
rm -f "wp-login.php?action=lostpassword"
rm -f "xmlrpc.php?rsd"

echo "Replacing hostname..."

find . -type f -exec sed -i 's|https://wordpress.fs-uae.net|https://fs-uae.net|g' {} +
find . -type f -exec sed -i 's|https:\\/\\/wordpress.fs-uae.net|https:\\/\\/fs-uae.net|g' {} +
find . -type f -exec sed -i 's|https%3A%2F%2Fwordpress.fs-uae.net|https%3A%2F%2Ffs-uae.net|g' {} +

echo
echo "OK."
