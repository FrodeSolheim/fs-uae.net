---
layout: option
title: joystick_port_3_mode
tags: [docs, options]

default: nothing
example: joystick
---

Specify what emulated Amiga device is connected to joystick port 3.
Valid values are:

* joystick
* nothing

Code:

    if c.joystick_port_3_mode.explicit:
        value = c.joystick_port_3_mode.explicit
    else:
        # FIXME: depends on actual device in joystick_port_3...?
        value = "nothing"
