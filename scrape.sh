#!/bin/sh

# set -e

mkdir -p scrape
cd scrape && \
wget --recursive --no-host-directories \
	--trust-server-names \
	--exclude-directories=files,wp-json \
	https://fs-uae.net/download

echo "Scraping done, removing some files..."

rm -f "robots.txt"
rm -f "wp-login.php"
rm -f "wp-login.php?action=lostpassword"
rm -f "xmlrpc.php?rsd"

echo
echo "OK."
