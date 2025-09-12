---
layout: option
title: uae_cd32cd
tags: [docs, options]

---

Code:
    if c.uae_cd32cd.explicit:
        # FIXME: boolean
        value = c.uae_cd32cd.explicit
    elif c.int_model == "CD32":
        value = "true"
    else:
        value = "false"
