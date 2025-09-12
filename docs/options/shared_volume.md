---
layout: option
title: shared_volume
tags: [docs, options, fsuae_option]

description: Add shared volume
default: 0
example: 1
type: Boolean
---

FIXME: TODO: Implement support for this

Enable this option to automatically add a shared volume (`Shared:`) to the
emulated Amiga. This is a directory hard drive and will also enable the UAE boot
ROM.

The volume will be added after all other hard drives. Therefore, the device
name (DHx:) can change if you add other drives. The recommended way to access
this volume is by using the volume name `Shared:`.
