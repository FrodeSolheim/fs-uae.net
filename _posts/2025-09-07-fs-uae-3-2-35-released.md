---
layout: post
title: FS-UAE 3.2.35 released
---

Version 3.2.35:

- Fix crash caused when opening the "More..." input menu.

Version 3.2.x:

- Disable cpu governor warning on Linux.
- Allow overriding device names for hard drive directories.
- Upgrade libslirp to version 4.6.1.
- Backported builtin slirp from FS-UAE 4 (fixes A2065 instability).
- Use g_get_monotonic_time() for high-resolution time on Windows as well.

Builds are available on [github](https://github.com/FrodeSolheim/fs-uae/releases/tag/v3.2.35). The download section on fs-uae.net will be updated later.

[Linux package repositories](https://software.opensuse.org/download.html?project=home%3AFrodeSolheim&package=fs-uae) are also available.
