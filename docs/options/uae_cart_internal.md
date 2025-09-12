---
layout: option
title: uae_cart_internal
tags: [docs, options, uae_option]

default:
example: hrtmon
since: 2.5.13
---

Built-in cartridge ROM
Tags: deprecated, emulation

Value: hrtmon

Using uae_cart_internal = hrtmon is the same as uae_cart_file = :HRTMon.

Deprecation notice. This value is (probably) deprecated. WinUAE does not save
this option to .uae config files. Instead, it saves uae_cart_file = :HRTMon.
