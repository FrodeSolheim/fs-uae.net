---
layout: option
title: whdload_splash_delay
tags: [docs, options]

description: Override WHDLoad splash delay
default: 200
example: 0
type: integer
---

Range: -1 - 500

This option specifies the time in 1/50ths seconds that WHDLoad shows the
information window at startup. If SplashDelay/K/N is lower than
ReadDelay/K/N it is ignored and the window is displayed using the time from
ReadDelay/K/N. The window is displayed at least as long as Preload/S is
processing.

If the option is set to 0 no window will be displayed at all. If the option
is set to -1 a Start button is added to the window and it remains open until
this button has been pressed.
