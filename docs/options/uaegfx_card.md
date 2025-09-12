---
layout: option
title: uaegfx_card
tags: [docs, options]

description: Deprecated: uaegfx_card
default: 0
example: 1
since: 1.3.28
type: boolean
---

Deprecated: Use [graphics_card] instead.

This option enables a Zorro III RTG graphics card which can be used with
Picasso96 drivers to open high-resolution and high-color displays on
Amiga.

This option must be used with a CPU with 32-bit addressing, which
means you must use the A1200/020 or A4000/040 models.

Code:

    if c.uaegfx_card.explicit:
        # FIXME: check boolean
        value = c.uaegfx_card.explicit
    else:
        value = ""
