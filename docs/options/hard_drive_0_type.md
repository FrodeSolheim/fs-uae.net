---
layout: option
title: hard_drive_0_type
tags: [docs, options, fsuae_option]

default: auto
example: rdb
since: 2.1.1
---

This option can be used to enable RDB mode for an empty HDF file (which
is missing the RDSK header). You may need to use this option in order to
partition the HDF file from the Amiga side, but on susequent use, FS-UAE
should automatically detect the HDF files as an RDB file, and this option
is no longer needed for that file.
