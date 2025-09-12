---
layout: option
title: int_cpuboardmem1_size
tags: [docs, options, fsuae_option]

---

Code:

    if c.accelerator_memory:
        value = str(int(c.accelerator_memory) * 1024)
    else:
        value = "0"
