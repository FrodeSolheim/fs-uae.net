---
layout: option
title: uae_immediate_blits
tags: [docs, options]

default: false
example: true
type: boolean-uae
---

Immediate Blitter

Tags: emulation

Faster but less compatible blitter emulation.

Immediate blitter [uae_immediate_blits] and waiting blits [uae_waiting_blits]
can't be enabled simultaneously. If immediate blitter is enabled, waiting
blits will be forcefully disabled.
