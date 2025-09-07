import json
import os
import sys
from typing import Any, TypedDict

from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape


class Vars(TypedDict):
    latestVersion: str
    discordServerInviteLink: str
    downloads: Any  # FIXME: For now


def main():
    global staticMap
    # staticMap = build_static_map()
    # env = Environment(loader=PackageLoader("app"), autoescape=select_autoescape())
    env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())
    vars = load_vars()
    # vars["contentOnly"] = False

    # process(env, vars, "public_html")
    process(env, vars, "public_html")

    # vars["contentOnly"] = True
    # process(env, vars, "public_html/__content__")
    # FIXME: Write .htaccess file with content forbiddein in __content__ ?
    # (Not very important though)
    # Or just add to robots to txt

    # fix_static_in("public_html/wp-content/themes/fs-uae")
    # fixStaticIn("public_html/wp-content/themes/fs-uae")


def process(env: Environment, vars: Vars, output_dir: str):
    if len(sys.argv) > 1:
        for fileName in sys.argv[1:]:
            print(fileName)
            process_file(env, fileName, vars, output_dir)
    else:
        # process_dir(env, "generated", vars, output_dir)
        # process_dir(env, "redirects", vars, output_dir)
        process_dir(env, "templates/scraped", vars, output_dir)


def process_dir(env: Environment, dir_name: str, vars: Vars, output_dir: str):
    for dirPath, _, fileNames in os.walk(dir_name):
        for fileName in fileNames:
            # processFile(env, fileName, vars)
            filePath = os.path.join(dirPath, fileName)
            process_file(env, filePath, vars, output_dir)


def process_file(env: Environment, file_path: str, vars: Vars, out_dir: str) -> None:
    if not file_path.endswith(".html"):
        return
    print("process_file", file_path)
    dir_name = file_path.split("/", 1)[0]
    template_path = file_path

    assert template_path.startswith(f"{dir_name}/")
    template_path = template_path[len(f"{dir_name}/") :]

    template_path = f"{dir_name}/{template_path}"

    print("template_path:", template_path)
    if template_path.startswith("templates/"):
        template_path = template_path[10:]
    # template_path = "/home/frode/git/fs-uae.net/" + template_path

    template = env.get_template(template_path)
    html = template.render(**vars)

    # FIXME: Inefficient...
    # for before, after in staticMap.items():
    #     html = html.replace(before, after)

    # Remove first directory level
    parts = template_path.split("/", 1)
    out_name = "/".join(parts[1:])

    if out_name == "index.html":
        out_path = os.path.join(out_dir, "index.html")
    # elif out_dir == "public_html":
    #     out_path = os.path.join(out_dir, template_path[:-5], "index.html")
    else:
        out_path = os.path.join(out_dir, out_name[:-5], "index.html")
        # out_path = os.path.join(out_dir, out_name)

    if not os.path.exists(os.path.dirname(out_path)):
        os.makedirs(os.path.dirname(out_path))
    with open(out_path, "w", encoding="UTF-8") as f:
        f.write(html)


def load_downloads() -> Any:
    downloads = {}  # type: ignore
    return downloads  # type: ignore

    # def addVersion(key, version, url, name, size, sha256):
    #     if size < 10 * 1024:
    #         sizeDescription = f"{size / (1024 * 1024):0.2f} MB"
    #     elif size < 10 * 1024 * 1024:
    #         # sizeDescription = str(round(size / (1024))) + " KB"
    #         sizeDescription = f"{size / (1024 * 1024):0.1f} MB"
    #     else:
    #         sizeDescription = str(round(size / (1024 * 1024))) + " MB"
    #     downloads[key] = {
    #         "name": name,
    #         "sha256": sha256,
    #         "size": size,
    #         "sizeDescription": sizeDescription,
    #         "version": version,
    #         "url": url,
    #     }

    # with open("updates/v2/updates.json", "r", encoding="UTF-8") as f:
    #     doc = json.load(f)
    # for package, info in doc.items():
    #     files = info["files"]
    #     for file in files:
    #         _, ext = os.path.splitext(file["name"])
    #         if ext == ".xz" and file["name"].endswith(".tar.xz"):
    #             ext = ".tar.xz"
    #         name = f'{package}_{file["branch"]}_{file["system"]}{ext}'
    #         addVersion(
    #             name,
    #             file["version"],
    #             file["url"],
    #             file["name"],
    #             file["size"],
    #             file["sha256"],
    #         )
    #     for branch in info["branches"]:
    #         if "latestSource" in info["branches"][branch]:
    #             file = info["branches"][branch]["latestSource"]
    #             name = f'{package}_{file["branch"]}_Source.tar.xz'
    #             addVersion(
    #                 name,
    #                 file["version"],
    #                 file["url"],
    #                 file["name"],
    #                 file["size"],
    #                 file["sha256"],
    #             )
    # return downloads


def load_vars() -> Vars:
    vars: Vars = {
        "downloads": load_downloads(),
        "latestVersion": "3.1",
        "discordServerInviteLink": "https://discord.gg/JZNCv27YqV",
    }
    # vars["latestVersion"] = "3.1"
    # # vars["latestDevelopmentVersion"] = "2.9.12dev"
    # vars["downloads"] = load_downloads()
    # vars["discordServerInviteLink"] = "https://discord.gg/JZNCv27YqV"

    # vars["downloads"] = {
    #     "FS-UAE_Stable_Windows_x86-64": {
    #         "url": "a",
    #         "name": "b",
    #     }
    # }

    # downloads['FS-UAE_Stable_Windows_x86-64'].url }}">{{ downloads['FS-UAE_Stable_Windows_x86-64'].name

    return vars


def build_static_map():
    # staticMap = {}
    # # FIXME: Load from json?
    # sDir = os.path.join("public_html", "s")
    # for dirPath, dirNames, fileNames in os.walk(sDir):
    #     for fileName in fileNames:
    #         filePath = os.path.join(dirPath, fileName)
    #         if fileName.endswith(".sha1"):
    #             with open(filePath, "r") as f:
    #                 # name = fileName[:-5]
    #                 sha1 = f.read().strip()
    #                 orig = filePath[len("public_html/"):-5]
    #                 staticMap[orig] = f"{orig}.v/{sha1}/{fileName[:-5]}"
    # print(staticMap)

    with open(os.path.join("public_html", "s", "versioned.json"), "r") as f:
        staticMap = json.load(f)
    return staticMap


# def fix_static_in(directory: str) -> None:
#     for dirPath, _, fileNames in os.walk(directory):
#         for fileName in fileNames:
#             path = os.path.join(dirPath, fileName)
#             _, ext = os.path.splitext(path)
#             if not ext in [".css", ".php", ".html"]:
#                 continue
#             with open(path, "r", encoding="UTF-8") as f:
#                 oldText = f.read()
#             text = oldText
#             # print(path)
#             # FIXME: Inefficient...
#             for before, after in staticMap.items():
#                 text = text.replace(before, after)
#             if text != oldText:
#                 print("Fixed", path)
#                 with open(path, "w", encoding="UTF-8") as f:
#                     f.write(text)


if __name__ == "__main__":
    main()
