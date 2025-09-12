---
layout: option
title: uae_slirp_implementation
tags: [docs, options, uae_option]

description: Slirp Implementation
default: auto
example: qemu
type: Choice
---

Value: auto
Value: none
Value: builtin
Value: qemu

Code:
    if c.uae_slirp_implementation.explicit:
        # FIXME: ok? keep already specified value
        value = c.uae_slirp_implementation.explicit
        # FIXME: check value
    else:
        value = "auto"
