#!/bin/sh

# set -e

mkdir -p scrape
cd scrape && \
wget \
	--mirror \
	--no-host-directories \
	--trust-server-names \
	--exclude-directories=files,wp-json \
	-e robots=off \
	https://wordpress.fs-uae.net/

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
