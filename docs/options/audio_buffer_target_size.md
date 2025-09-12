---
layout: option
title: audio_buffer_target_size
tags: [docs, options, fsuae_option]

description: Audio buffer target size (ms)
default: 40
example: 20
since: 2.3.14
type: integer
---

Range: 1 - 100

Specify the target size for FS-UAE’s audio buffer. The default value
(if not specified) is currently 40 ms.

Higher values will give you more stable sound, but at the expense of higher
latency. Too low values will cause frequent buffer under-runs (stuttering
audio output). The default value is a compromise between latency and
stability, but you may be able to get stable audio output with a lot
smaller buffer depending on your system.

Note: This is FS-UAE's internal audio buffer. OpenAL and lower level audio
drivers may have their own buffers, which you may also be able to tweak
separately.
