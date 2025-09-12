---
layout: option
title: uae_cpu_throttle
tags: [docs, options, uae_option]

description: FIXME
default:
type: float
---

Range: -900.0 - 5000.0

FIXME: describe what it does

In cycle-exact-mode, this option cannot be used and is locked to 0.0.

In approximate mode, this option can be used with the range -900.0 - 5000.0
to speed up or slown down the emulated CPU. In fastest-possible mode,
you can only use this option to slow down the emulation (-900.0 - 0).

See: [cpu_idle]
