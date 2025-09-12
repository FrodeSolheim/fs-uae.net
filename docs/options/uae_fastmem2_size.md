---
layout: option
title: uae_fastmem2_size
tags: [docs, options]

description: Size in MB of Zorro-II Fast RAM (second) expansion board
default: 0
type: choice
---

Value: 0
Value: 1
Value: 2
Value: 4

Size must be smaller or same as first fast memory board (WinUAE v2.8.2 Beta 1 Changelog).

The memory will be added as a autoconfig board named "Z2Fast2" unless [uae_fastmem_autoconfig] is disabled.

Use [uae_fastmem2_size_k] to specify sizes below 1 MB.

See [uae_fastmem_size], [uae_fastmem_autoconfig]
