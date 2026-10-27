# holykeebs QMK userspace

This repo is a [QMK External Userspace](https://docs.qmk.fm/newbs_external_userspace)
overlay carrying the `users/holykeebs` userspace — the cross-keyboard holykeebs
functionality (pointing-device handling for Pimoroni trackball, TrackPoint,
Cirque, Azoteq TPS and PMW3360; sniping, drag-scroll, scroll lock, OLED, EEPROM
config, split state sync).

It is the **single source of truth** for `users/holykeebs`, shared by the
holykeebs forks of both [qmk_firmware](https://github.com/qmk/qmk_firmware) and
[vial-qmk](https://github.com/vial-kb/vial-qmk) so the userspace isn't
maintained as two copies.

The keyboards themselves (`keyboards/holykeebs/*`) live in those forks, not here —
QMK External Userspace overlays `users/` (and keymaps), not whole keyboards.

## Setup

Point a local QMK checkout at this overlay (the setting is global to the `qmk`
CLI, so it applies to every fork you build):

```
qmk config user.overlay_dir="/path/to/holykeebs-userspace"
```

After that, build from inside the fork as usual. The userspace is still selected
explicitly with `USER_NAME=holykeebs` (the keyboards include it by full path):

```
make holykeebs/keyball61plus:via -e USER_NAME=holykeebs -e OLED=yes -e OLED_FLIP=yes
```

The build system prefers `<overlay>/users/holykeebs` over any in-tree copy, so
this overlay wins even if a stale `users/holykeebs` is still present in a fork.

See each fork's `CLAUDE.md` for the full holykeebs build-variable reference.

## schlechter32's Lily58 keymap

Trackpoint (left) + TPS43 touchpad (right), ported from a ZMK Corne layout: see the
[keymap and flashing guide](keyboards/holykeebs/lily58/keymaps/schlechter32/readme.md).
