---
layout: option
title: keyboard_input_grab
tags: [docs, options]

description: Grab keyboard when input is grabbed
default: 1
example: 0
since: 2.3.10
type: boolean
---

Set this option to 0 to prevent input grab from also grabbing the keyboard,
only the mouse will then be grabbed. This only works when FS-UAE uses
SDL2. By default, both mouse and keyboard input will be grabbed together.
