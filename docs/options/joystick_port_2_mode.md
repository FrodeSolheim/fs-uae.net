---
layout: option
title: joystick_port_2_mode
tags: [docs, options]

default: nothing
example: joystick
---

Specify what emulated Amiga device is connected to joystick port 2.
Valid values are:

* joystick
* nothing

Code:

    if c.joystick_port_2_mode.explicit:
        value = c.joystick_port_2_mode.explicit
    else:
        # FIXME: depends on actual device in joystick_port_2...?
        value = "nothing"
