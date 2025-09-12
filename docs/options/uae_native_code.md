---
layout: option
title: uae_native_code
tags: [docs, options]

---

Code:

    if c.uae_native_code.explicit:
        value = c.uae_native_code.explicit
    elif c.uaenative_library == "1":
        value = "true"
    else:
        value = "false"
