---
layout: option
title: uae_cpu_frequency
tags: [docs, options, uae_option]

description: Specify the frequency of the emulated CPU in cycle-exact modes
default:
example: 14187580
type: integer
---

# Range: 1.0 - 100.0

When [uae_cpu_multiplier] option is set to 0, use this option to specify
the CPU frequency manually. If [uae_cpu_multiplier] is non-0, this option
will be ignored.

This option is only intended to be used with cycle-exact CPU.
