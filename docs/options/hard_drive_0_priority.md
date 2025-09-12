---
layout: option
title: hard_drive_0_priority
tags: [docs, options]

default: 0
example: 6
since: 2.1.26
---

By default, for hard drives, the boot priority is set to 0. You can override
this to change the boot order. For example, set boot priority to 6 to move
the HD before DF0 in the boot order.

This works for single-partition HDF images and directory hard drives. If
you use full hard drive images (RDB HDFs), you need to specify the boot
priorities on the partitions from within the Amiga instead.
