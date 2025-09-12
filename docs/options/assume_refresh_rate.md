---
layout: option
title: assume_refresh_rate
tags: [docs, options, fsuae_option]

default:
example: 50
since: 2.2.2
---

Use this option to manually specify host refresh ate when refresh rate
detection fails. This option in combination with video_sync = auto
effectively replaces the old feature where you can use video_sync = full
to force full vsync.
