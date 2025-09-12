---
layout: option
title: uae_cpu_speed
tags: [docs, options, uae_option]

description: Enable/disable fastest possible CPU speed
default:
example: max
type: choice
---

Value: real ("Approximate A500/A1200 or cycle-exact")
Value: max ("Fastest possible")

The default value is "real" for <= 68020-based models, and "max" for
high-end Amiga models (68030/68040-based models).

As an alternative to this option, you can use [uae_finegrain_cpu_speed].

See: [uae_cpu_multiplier], [uae_cpu_throttle], [cpu_idle]
