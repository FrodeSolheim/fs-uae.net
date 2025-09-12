---
layout: option
title: frame_time
tags: [docs, options]

description: Frame time (ms)
default: 0
example: 10
since: 2.9.7
---

Specify how long FS-UAE is allowed to emulate and render a frame. This can be
used to force FS-UAE to pause after v-sync, before it starts emulating a new
frame.

If you are running in PAL emulation, you can for example specify 13 to make
FS-UAE wait 7 ms after a frame is done, before it starts emulating the next
one.

This option is not tested in all circumstances, and will interfere with
fastest-possible modes, etc. The option is not supported in net play mode.
