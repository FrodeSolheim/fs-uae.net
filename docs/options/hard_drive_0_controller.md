---
layout: option
title: hard_drive_0_controller
tags: [docs, options]

default: uae
example: ide0
since: 2.1.1
---

You can use this option to specify the HD controller for this drive, for
example to use an emulated IDE controller for A600/A1200.

Warning: Using IDE instead of the default UAE controller is slower, and
lacks features compared to the UAE controller. Also, you risk silently
losing data with drives >= 4GB due 32-bit wraparound (lack of full 64-bit
addressing support).
