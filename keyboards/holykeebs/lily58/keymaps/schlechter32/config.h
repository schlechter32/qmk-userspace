// Copyright 2026 schlechter32
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

// Home-row mods, ported from the ZMK "balanced" hold-taps. These are the defaults applied to
// Vial's QMK Settings after a flash (keymap.c); the QMK Settings tab can retune them.
#define TAPPING_TERM 280
#define QUICK_TAP_TERM 175     // ZMK quick-tap-ms
#define HRM_FLOW_TAP_TERM 150  // ZMK require-prior-idle-ms

#define DYNAMIC_KEYMAP_LAYER_COUNT 6

// Layer colours on the half without USB. The userspace only syncs layer state with an OLED.
#define SPLIT_LAYER_STATE_ENABLE

// Split RPC used to flash the half without USB (keymap.c). Keep the userspace's own ids.
#ifdef SPLIT_TRANSACTION_IDS_USER
#    if defined(HK_SPLIT_SYNC_STATE) && defined(HK_SPLIT_DETECT_POINTING)
#        undef SPLIT_TRANSACTION_IDS_USER
#        define SPLIT_TRANSACTION_IDS_USER HK_SYNC_STATE, HK_GET_POINTING_INFO, KM_FLASH_SYNC
#    elif defined(HK_SPLIT_SYNC_STATE)
#        undef SPLIT_TRANSACTION_IDS_USER
#        define SPLIT_TRANSACTION_IDS_USER HK_SYNC_STATE, KM_FLASH_SYNC
#    else
#        undef SPLIT_TRANSACTION_IDS_USER
#        define SPLIT_TRANSACTION_IDS_USER HK_GET_POINTING_INFO, KM_FLASH_SYNC
#    endif
#else
#    define SPLIT_TRANSACTION_IDS_USER KM_FLASH_SYNC
#endif

// Vial identity (same as holykeebs' stock Lily58 Vial keymap) and unlock combo.
#define VIAL_KEYBOARD_UID {0x51, 0x87, 0x4D, 0xF7, 0xD7, 0x45, 0xD5, 0xF0}
#define VIAL_UNLOCK_COMBO_ROWS { 0, 5 }
#define VIAL_UNLOCK_COMBO_COLS { 0, 0 }
