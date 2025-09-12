---
layout: option
title: uae_sana2
tags: [docs, options]

description: uae_sana2
default: false
example: true
type: BooleanUAE,
---

Code:
    if c.uae_sana2.explicit:
        # FIXME: ok? keep already specified value
        value = c.uae_rtc.explicit
        # FIXME: match and normalize uae boolean
    else:
        value = "false"
