#!/usr/bin/env bash
# Build and flash the holykeebs Lily58 halves (RP2040, UF2) one after the other, without root.
# TRRS can stay connected; never plug or unplug it while USB is connected.
#
# Usage: util/flash_lily58.sh [--build] [keymap]
#   keymap defaults to schlechter32. --build rebuilds both halves (and the keymap docs) first.
#   QMK_FIRMWARE defaults to ../holykeebs-vial-qmk (holykeebs/vial-qmk, branch hk-master).

set -euo pipefail

cd "$(dirname "$0")/.."
USERSPACE="$PWD"

BUILD=no
if [[ "${1:-}" == "--build" ]]; then
    BUILD=yes
    shift
fi
KEYMAP="${1:-schlechter32}"
POINTING_DEVICE="${POINTING_DEVICE:-trackpoint_tps43}"
FIRMWARE="${QMK_FIRMWARE:-$(realpath ../holykeebs-vial-qmk)}"
LABEL="RPI-RP2"

fw_file() { echo "$USERSPACE/holykeebs_lily58_${KEYMAP}_${POINTING_DEVICE}_$1.uf2"; }

if [[ "$BUILD" == yes ]]; then
    export QMK_HOME="$FIRMWARE" QMK_FIRMWARE="$FIRMWARE" QMK_USERSPACE="$USERSPACE" PYTHONPATH="$FIRMWARE/lib/python"
    export PATH="$FIRMWARE/bin:$HOME/opt/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi/bin:$HOME/.venvs/qmk/bin:$PATH"
    for side in left right; do
        make -C "$FIRMWARE" "holykeebs/lily58:$KEYMAP" -e USER_NAME=holykeebs -e POINTING_DEVICE="$POINTING_DEVICE" \
            -e SIDE="$side" -e TARGET="$(basename "$(fw_file "$side")" .uf2)" -e SKIP_GIT=yes -j8
    done
    python3 util/lily58_keymap_doc.py
fi

for side in left right; do
    if [[ ! -f "$(fw_file "$side")" ]]; then
        echo "Missing $(fw_file "$side") - run with --build first." >&2
        exit 1
    fi
done

# Prints the mount point of the RP2040 bootloader drive, mounting it if needed.
mount_bootloader() {
    local dev mnt
    dev="$(readlink -f "/dev/disk/by-label/$LABEL" 2>/dev/null || true)"
    [[ -b "$dev" ]] || return 1
    mnt="$(findmnt -nro TARGET -S "$dev" || true)"
    if [[ -z "$mnt" ]]; then
        udisksctl mount -b "$dev" >/dev/null
        mnt="$(findmnt -nro TARGET -S "$dev")"
    fi
    echo "$mnt"
}

flash_side() {
    local side="$1" fw mnt="" i
    fw="$(fw_file "$side")"
    echo "Waiting for the $LABEL drive..."
    for i in $(seq 1 20); do
        if mnt="$(mount_bootloader)"; then
            break
        fi
        sleep 0.5
    done
    if [[ -z "$mnt" ]]; then
        echo "No $LABEL drive found. Is the $side half really in bootloader mode?" >&2
        return 1
    fi
    echo "Copying $(basename "$fw") to $mnt"
    cp "$fw" "$mnt/"
    sync
    # The RP2040 reboots into the new firmware once the UF2 is written; wait for the drive to go away.
    for i in $(seq 1 20); do
        [[ -e "/dev/disk/by-label/$LABEL" ]] || break
        sleep 0.5
    done
    echo "$side half flashed."
}

echo "Flashing holykeebs/lily58:$KEYMAP ($POINTING_DEVICE). Keep TRRS connected; only plug or unplug it with USB disconnected."
echo "Keymap-only changes just need the left half (answer n for the right)."
echo "Bootloader: LOWER+RAISE then Esc or Backspace reboots the half that has USB (or double-tap reset)."
echo "Right half: move the USB cable to it first. Never connect USB to both halves at once."
echo

for side in left right; do
    while true; do
        read -r -p "${side^^} half: USB in the $side half and in bootloader ($LABEL drive)? [y]es / [n]o, skip / [q]uit: " answer
        case "$answer" in
            y|Y) if flash_side "$side"; then break; fi ;;
            n|N) echo "Skipping $side half."; break ;;
            q|Q) exit 0 ;;
        esac
    done
    echo
done

echo "Done. If USB is in the right half, move it back to the LEFT half."
