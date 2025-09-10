---
layout: scraped
title: Log files
permalink: /logging/
# FIXME: MAYBE MOVE TO docs! /docs/logging ? (and leave the redirects in place)
---

# Logging

FS-UAE logs some information by default to log files which may aid in investigating issues. The location of the log files, `fs-uae.log.txt` and `fs-uae-launcher.log.txt`, may vary slightly from system to system:

- The log files are generally found in `(My) Documents/FS-UAE/Cache/Logs`.
- If you are using the portable version, they'll be in `Cache/Logs` within the portable directory.
- On Linux, might also find them in `~/FS-UAE/Cache/Logs` if `XDG_DOCUMENTS_DIR` is not set.

## Including log files when reporting an issue

When reporting issues with FS-UAE or FS-UAE Launcher, you may be asked
to provide log files to help debugging the problem (or
clear up any misunderstandings). Some important things to consider:

- Before attaching the log files, you _must_ quit FS-UAE and/or FS-UAE Launcher. If not, the log files may be
  incomplete.
- The log files are recreated each time you start the program. So when reporting a problem, you must ensure that you experienced the problem on the last run of the program.

If you're reporting a problem on the [English Amiga Board forum](ttps://eab.abime.net/forumdisplay.php?f=122) it's easy to include the log files. When writing a reply or creating a thread, you can attach the log files to the post.

If you are asked to send log files by e-mail, please send to [frode@fs-uae.net](mailto:frode@fs-uae.net).
