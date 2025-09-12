---
layout: option
title: cpu_idle
tags: [docs, options, fsuae_option]

description: Relax host CPU usage when using fastest-possible CPU
default:
example: 3
type: integer
---

Range: 0 - 10

When using fastest-possible CPU mode, the UAE core will, without idling,
use as much host CPU as possible. This setting controls how often UAE
performs a short sleep when 68000 STOP instructions are executed.

The default value for fastest-possible mode is 2. For exact or approximate
CPU speeds, cpu_idle is not used.

See: [uae_cpu_throttle]
