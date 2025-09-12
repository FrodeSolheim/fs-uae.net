---
layout: option
title: texture_filter
tags: [docs, options, fsuae_option]

description: Texture filter
default: linear
example: nearest
since: 1.3.8
type: choice
---

FS-UAE by default renders the Amiga display as a texture with texture filter
set to GL_LINEAR. You can use this option to force GL_NEAREST filter.

Value: nearest (GL_NEAREST)
Value: linear (GL_LINEAR)
