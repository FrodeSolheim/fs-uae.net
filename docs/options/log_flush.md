---
layout: option
title: log_flush
tags: [docs, options, fsuae_option]

description: Flush log after each log line
type: boolean
---

Flushing the log after each log line may affect performance, but will
ensure the latest log lines are actually written when/if FS-UAE crashes.
