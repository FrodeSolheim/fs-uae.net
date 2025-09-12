---
layout: option
title: uae_cd32fmv
tags: [docs, options]

---

Code:
    if c.uae_cd32fmv.explicit:
        # FIXME: boolean
        value = c.uae_cd32fmv.explicit
    elif c.amiga_model == "CD32/FMV":
        value = "true"
    else:
        value = "false"
