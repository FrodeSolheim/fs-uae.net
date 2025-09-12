---
layout: option
title: int_z3fastmem_size
tags: [docs, options, fsuae_option]

---

Code:

    if int(c.uae_z3mem_size):
        value = str(int(c.uae_z3mem_size) * 1024 * 1024)
    # if c.zorro_iii_memory:
    #     value = str(int(c.zorro_iii_memory) * 1024)
    else:
        value = "0"
