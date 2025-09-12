---
layout: option
title: dongle_type
tags: [docs, options, fsuae_option]

description: Hardware Dongle
default: 0
example: robocop 3
since: 2.1.33
type: Choice
---

If a game requires an emulated hardware dongle, set dongle_type to one
of these values:

Value: 0 ("None")
Value: robocop 3 (RoboCop 3)
Value: leaderboard (Leader Board)
Value: b.a.t. ii (B.A.T. II)
Value: italy'90 soccer (Italy Soccer '90)
Value: dames grand maitre (Dames Grand-Maître)
Value: rugby coach (Rugby Coach)
Value: cricket captain (Cricket Captain)
Value: leviathan (Leviathan)

Code:

    # FIXME: uae_dongle_type
    if c.dongle_type.explicit:
        c.dongle_type = c.dongle_type.explicit
    else:
        c.dongle_type = "0"
