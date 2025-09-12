#!/usr/bin/env python3

import os
import re


def import_option(path: str) -> None:
    if os.path.isdir(path):
        return

    with open(path, "r") as f:
        text = f.read()
    name = os.path.basename(path)
    dest = os.path.join("docs", "options", name)

    dest_html = dest + ".html"
    if os.path.exists(dest_html):
        os.unlink(dest_html)   
    dest_html_u = dest_html.replace("_", "-")
    if os.path.exists(dest_html_u):
        os.unlink(dest_html_u)

    allowed_keys = ["Description", "Summary", "Type", "Default", "Example", "Since"]
    key_re = re.compile(rf'^\s*(?P<key>{"|".join(map(re.escape, allowed_keys))}):\s*(?P<val>.*)$')

    data = {}
    kept_lines = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip("\r\n")
        # skip full-line comments
        if re.match(r'^\s*//', line):
            kept_lines.append(raw_line)
            continue

        m = key_re.match(line)
        if not m:
            kept_lines.append(raw_line)
            continue

        key = m.group('key')
        val = m.group('val')

        # strip inline comments
        val = re.sub(r'\s*//.*$', '', val).strip()

        # strip surrounding matching quotes
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ('"', "'"):
            val = val[1:-1]

        data[key] = val  # last one wins; change to list if you need multiples

    cleaned_text = "\n".join(kept_lines).strip()

    text = cleaned_text

    # pattern = r'(?m)^(\w+):\s*("?[^"\n]+"?|[^\n]+)$'
    # matches = re.findall(pattern, text)

    # Convert to dictionary
    # data = {key: value.strip('"') for key, value in matches}

    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")

    text = text.strip("\n")
    # if not text.endswith("\n"):
    #     text = text + "\n"

    dest_md = dest + ".md"
    with open(dest_md, "w") as f:
        f.write("---\n")
        f.write("layout: option\n")
        f.write(f"title: {name}\n")
        # f.write("permalink: /docs/options/\n")
        f.write("tags: [docs, options]\n")
        f.write("\n")
        if "Description" in data:
            f.write(f"description: {data["Description"]}\n")
        elif "Summary" in data:
            f.write(f"description: {data["Summary"]}\n")

        if "Default" in data:
            f.write(f"default: {data["Default"]}".strip())
            f.write("\n")
        if "Example" in data:
            f.write(f"example: {data["Example"]}\n")
        if "Since" in data:
            f.write(f"since: {data["Since"]}\n")
        if "Type" in data:
            f.write(f"type: {data["Type"]}\n")

        # f.write(repr(data))
        f.write("---\n")
        if text:
            f.write("\n")
            f.write(text)
            f.write("\n")


for item in os.listdir("../fs-uae-3/doc/options"):
    import_option(os.path.join("../fs-uae-3/doc/options", item))

for item in os.listdir("../fs-uae-3/docs/options"):
    import_option(os.path.join("../fs-uae-3/docs/options", item))
