---
layout: option
title: cdrom_drive_count
tags: [docs, options, fsuae_option]

description: CD-ROM Drive Count
default:
example: 1
type: Choice
---

Value: 0
Value: 1

Code:
    if c.cdrom_drive_count.explicit:
        value = c.cdrom_drive_count.explicit
    elif c.cdrom_drive_0:
        value = "1"
    elif c.cdrom_image_0:
        value = "1"
    elif c.int_model == "CD32":
        value = "1"
    elif c.int_model == "CDTV":
        value = "1"
    else:
        value = "0"
