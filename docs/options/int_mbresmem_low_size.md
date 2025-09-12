---
layout: option
title: int_mbresmem_low_size
tags: [docs, options, fsuae_option]

---

Code:

    if int(c.uae_a3000mem_size):
        value = str(int(c.uae_a3000mem_size) * 1024 * 1024)
    else:
        value = "0"
