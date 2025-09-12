---
layout: option
title: int_z3chipmem_size
tags: [docs, options, fsuae_option]

---

Code:

    if int(c.uae_z3chipmem_size):
        value = str(int(c.uae_z3chipmem_size) * 1024 * 1024)
    else:
        value = "0"
