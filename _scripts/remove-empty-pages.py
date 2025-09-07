#!/usr/bin/env python3

import os

search = b"""\
</header>
<aside class="fs-page-comments">
<!--<div style="clear: both"></div>-->
<!--
<div style="
/*margin-top: 32px;*/
/*
margin-left: -32px;
margin-right: -32px;
padding-top: 32px;
padding-bottom: 16px;
padding-left: 32px;
padding-right: 32px;
background-color: white;
border-top: 6px solid #2f0c47;
*/
">
-->
<!--
</div>
-->
</aside>
<footer class="fs-site-footer">
"""


def main():
    for dir_path, _dir_names, file_names in os.walk("scrape"):
        for file_name in file_names:
            path = os.path.join(dir_path, file_name)
            with open(path, "rb") as f:
                data = f.read()
            if search in data:
                print("Detected empty page", path)
                os.remove(path)
                if len(os.listdir(dir_path)) == 0:
                    os.rmdir(dir_path)


if __name__ == "__main__":
    main()
