---
layout: option
title: jit_compiler
tags: [docs, options, fsuae_option]

description: JIT Compiler
default: 0
example: 1
type: Boolean
---

Code:

    if c.jit_compiler.explicit:
        c.jit_compiler = c.jit_compiler.explicit
    else:
        c.jit_compiler = "0"
