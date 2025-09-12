---
layout: option
title: int_ppc_model
tags: [docs, options]

---

Code:

    if f.matches(c.uae_cpuboard_type, "BlizzardPPC"):
        value = "603ev"
    elif f.matches(c.uae_cpuboard_type, "CyberStormPPC"):
        value = "604e"
    else:
        value = ""
