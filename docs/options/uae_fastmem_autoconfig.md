---
layout: option
title: uae_fastmem_autoconfig
tags: [docs, options]

description: Autoconfig Z2 Fast RAM
default: 1
example: 0
type: boolean
---

By default, fast memory is added as autoconfig expansion boards. You can use
this option to disable that and wire fast memory directly at 0x00200000 (
2nd fast memory bank, if any, will follow directly after).
