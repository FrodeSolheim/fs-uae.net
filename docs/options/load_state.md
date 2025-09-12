---
layout: option
title: load_state
tags: [docs, options]

description: Load state by number
default:
example: 5
since: 2.3.12
type: integer
---

Range: 1 - 9

Loads a save state identified by the save state slot number (1..9) when FS-UAE
starts. If the state does not exist, nothing will happen.
