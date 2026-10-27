 /* Copyright 2020 Naoki Katahira
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 2 of the License, or
  * (at your option) any later version.
  *
  * This program is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with this program.  If not, see <http://www.gnu.org/licenses/>.
  */

// Port of the ZMK corne keymap (zmk-config/config/corne.keymap) to the holykeebs Lily58.
// The Lily58-only keys (number row, inner keys, outer thumbs) carry the extras.

#include QMK_KEYBOARD_H
#include "holykeebs.h"
#include "pointing.h"
#include "transactions.h"
#include "qmk_settings.h"

enum layer_number {
  _BASE = 0,
  _LOWER,
  _RAISE,
  _ADJUST, // LOWER + RAISE
  _PLAIN,  // no home-row mods, toggled from RAISE
  _SPARE,  // free for Vial
};

// Home-row mods (ZMK hmmod / hmmodr / hmlayer / hmlayerr)
#define HM_A    LCTL_T(KC_A)
#define HM_S    LGUI_T(KC_S)
#define HM_D    LALT_T(KC_D)
#define HM_F    LT(_LOWER, KC_F)
#define HM_G    LT(_RAISE, KC_G)
#define HM_H    LT(_RAISE, KC_H)
#define HM_J    LT(_LOWER, KC_J)
#define HM_K    LALT_T(KC_K)
#define HM_L    RGUI_T(KC_L)
#define HM_SCLN RCTL_T(KC_SCLN)

// Tap O, hold for trackpoint drag-scroll (handled in process_record_keymap)
#define DS_O    LT(0, KC_O)

// Pinky shifts (ZMK pinkyshiftL / pinkyshiftR)
#define PS_TAB  LSFT_T(KC_TAB)
#define PS_ENT  RSFT_T(KC_ENT)

// Ctrl+Alt+Shift holds (ZMK SpaceMeh / slash)
#define MEH_SPC MEH_T(KC_SPC)
#define MEH_SLS MEH_T(KC_SLSH)

// Inner keys: tap [ / ], hold Ctrl+Shift. Fixes Ctrl (A) + Shift (Tab) both being on the left pinky
#define CS_LBRC C_S_T(KC_LBRC)
#define CS_RBRC C_S_T(KC_RBRC)

// LOWER mod-taps whose tap is a shifted symbol; the tap is sent in process_record_keymap
#define LM_PLUS LCTL_T(KC_EQL)
#define LM_CIRC LALT_T(KC_6)
#define LM_DLR  LGUI_T(KC_4)

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

 [_BASE] = LAYOUT(
  KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,                       KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_MINS,
  KC_ESC,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,                       KC_Y,    KC_U,    KC_I,    DS_O,    KC_P,    KC_BSPC,
  PS_TAB,  HM_A,    HM_S,    HM_D,    HM_F,    HM_G,                       HM_H,    HM_J,    HM_K,    HM_L,    HM_SCLN, PS_ENT,
  KC_DEL,  KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    CS_LBRC, CS_RBRC,  KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_QUOT, MEH_SLS,
                    MS_BTN1, KC_RALT, MO(_LOWER), MEH_SPC,      C(KC_BSPC), MO(_RAISE), KC_RALT, MS_BTN2
),

 [_LOWER] = LAYOUT(
  _______, _______, _______, _______, _______, _______,                    _______, _______, _______, _______, _______, _______,
  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   KC_F6,                      KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,  KC_F12,
  _______, KC_UNDS, LM_PLUS, LM_CIRC, LM_DLR,  _______,                    KC_LEFT, KC_DOWN, KC_UP,   KC_RGHT, KC_END,  _______,
  _______, KC_TILD, HK_D_MODE, MS_BTN3, HK_S_MODE, KC_F11, _______, _______, KC_HOME, KC_PGDN, KC_PGUP, KC_END,  KC_PGUP, _______,
                    _______, _______, _______, _______,                    _______, _______, _______, _______
),

 [_RAISE] = LAYOUT(
  _______, _______, _______, _______, _______, _______,                    _______, _______, _______, _______, _______, _______,
  _______, KC_AT,   KC_EXLM, KC_LCBR, KC_RCBR, KC_AMPR,                    KC_CIRC, KC_7,    KC_8,    KC_9,    KC_DLR,  _______,
  _______, KC_MINS, KC_BSLS, KC_LPRN, KC_RPRN, KC_ASTR,                    KC_0,    KC_4,    KC_5,    KC_6,    KC_EQL,  _______,
  _______, KC_GRV,  KC_HASH, KC_LBRC, KC_RBRC, KC_PERC, _______, _______,  KC_PIPE, KC_1,    KC_2,    KC_3,    KC_COMM, _______,
                    _______, TO(_PLAIN), _______, _______,                 _______, _______, _______, _______
),

// Pointer speed: hold sensitivity / sniping sensitivity / scroll throttle and press Down / Up. HK_SAVE keeps it.
 [_ADJUST] = LAYOUT(
  QK_CLEAR_EEPROM, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
  QK_BOOT, RM_TOGG, RM_NEXT, RM_HUED, RM_HUEU, HK_C_SCROLL,               XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, QK_BOOT,
  XXXXXXX, HK_P_SET_D, HK_P_SET_S, HK_P_SET_THR, HK_SAVE, HK_S_MODE_T,    XXXXXXX, KC_DOWN, KC_UP,   XXXXXXX, XXXXXXX, XXXXXXX,
  KC_LSFT, RM_VALD, RM_VALU, RM_SATD, RM_SATU, HK_D_MODE_T, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, HK_RESET, HK_DUMP, XXXXXXX,
                    _______, _______, _______, _______,                   _______, _______, _______, _______
),

 [_PLAIN] = LAYOUT(
  _______, _______, _______, _______, _______, _______,                    _______, _______, _______, _______, _______, _______,
  _______, KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,                       KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    _______,
  _______, KC_A,    KC_S,    KC_D,    KC_F,    KC_G,                       KC_H,    KC_J,    KC_K,    KC_L,    KC_SCLN, _______,
  _______, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    _______, _______,  KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_QUOT, _______,
                    _______, TO(_BASE), _______, _______,                  _______, _______, _______, _______
),

 [_SPARE] = LAYOUT(
  _______, _______, _______, _______, _______, _______,                    _______, _______, _______, _______, _______, _______,
  _______, _______, _______, _______, _______, _______,                    _______, _______, _______, _______, _______, _______,
  _______, _______, _______, _______, _______, _______,                    _______, _______, _______, _______, _______, _______,
  _______, _______, _______, _______, _______, _______, _______, _______,  _______, _______, _______, _______, _______, _______,
                    _______, _______, _______, _______,                    _______, _______, _______, _______
)
};

// Thumbs are '*' so they can trigger holds on either hand (ZMK lists the space thumb on both sides).
// The inner Ctrl+Shift keys are '*' too, so they work with keys on their own side.
const char chordal_hold_layout[MATRIX_ROWS][MATRIX_COLS] PROGMEM = LAYOUT(
  'L', 'L', 'L', 'L', 'L', 'L',                'R', 'R', 'R', 'R', 'R', 'R',
  'L', 'L', 'L', 'L', 'L', 'L',                'R', 'R', 'R', 'R', 'R', 'R',
  'L', 'L', 'L', 'L', 'L', 'L',                'R', 'R', 'R', 'R', 'R', 'R',
  'L', 'L', 'L', 'L', 'L', 'L', '*',      '*', 'R', 'R', 'R', 'R', 'R', 'R',
                 '*', '*', '*', '*',      '*', '*', '*', '*'
);

// RGB matrix: 35 LEDs per half (6 underglow + 29 per key). Each half draws its own LEDs.
// Non-BASE layers paint every LED in the layer colour; pointer feedback briefly overrides it.
static const uint8_t PROGMEM layer_hues[][3] = {
  [_LOWER]  = {HSV_BLUE},
  [_RAISE]  = {HSV_GREEN},
  [_ADJUST] = {HSV_PURPLE},
  [_PLAIN]  = {HSV_GOLD},
};

enum flash_colour { FLASH_UP, FLASH_DOWN, FLASH_SAVED };
static const uint8_t PROGMEM flash_hsv[][3] = {
  [FLASH_UP]    = {HSV_WHITE},
  [FLASH_DOWN]  = {HSV_RED},
  [FLASH_SAVED] = {HSV_CYAN},
};

static uint8_t  flash_colour;
static uint16_t flash_started;
static uint16_t flash_length; // 0 = no flash

static void flash_start(uint8_t colour, uint16_t ms) {
  flash_colour  = colour;
  flash_length  = ms;
  flash_started = timer_read();
}

// The half without USB draws its own LEDs, so its flashes are sent over TRRS.
typedef struct {
  uint8_t colour;
  uint8_t tens_of_ms;
} flash_msg_t;

static void flash_rpc_handler(uint8_t in_len, const void *in_data, uint8_t out_len, void *out_data) {
  const flash_msg_t *msg = in_data;
  flash_start(msg->colour, msg->tens_of_ms * 10);
}

// main = the USB half (left, trackpoint), peripheral = the other half (right, touchpad)
static void flash_half(bool peripheral, uint8_t colour, uint16_t ms) {
  if (peripheral) {
    flash_msg_t msg = {colour, ms / 10};
    transaction_rpc_send(KM_FLASH_SYNC, sizeof(msg), &msg);
  } else {
    flash_start(colour, ms);
  }
}

static void fill_hsv(uint8_t led_min, uint8_t led_max, uint8_t hue, uint8_t sat) {
  hsv_t hsv = {hue, sat, rgb_matrix_get_val()};
  rgb_t rgb = hsv_to_rgb(hsv);
  for (uint8_t i = led_min; i < led_max; i++) {
    rgb_matrix_set_color(i, rgb.r, rgb.g, rgb.b);
  }
}

bool rgb_matrix_indicators_advanced_user(uint8_t led_min, uint8_t led_max) {
  if (flash_length && timer_elapsed(flash_started) < flash_length) {
    fill_hsv(led_min, led_max, pgm_read_byte(&flash_hsv[flash_colour][0]), pgm_read_byte(&flash_hsv[flash_colour][1]));
    return false;
  }
  flash_length = 0;

  uint8_t layer = get_highest_layer(layer_state);
  if (layer != _BASE && layer < ARRAY_SIZE(layer_hues)) {
    fill_hsv(led_min, led_max, pgm_read_byte(&layer_hues[layer][0]), pgm_read_byte(&layer_hues[layer][1]));
  }
  return false;
}

// Vial's QMK Settings start with every tap-hold option off after a flash. Apply the ZMK-like
// defaults once; anything changed in Vial later is kept (unless it is all-off again).
static void apply_tap_hold_defaults(void) {
  if (QS.tapping_v2 != 0 || QS.flow_tap_term != 0) {
    return;
  }
  uint16_t tapping_term   = TAPPING_TERM;
  uint16_t quick_tap_term = QUICK_TAP_TERM;
  uint16_t flow_tap_term  = HRM_FLOW_TAP_TERM;
  uint8_t  on             = 1;
  qmk_settings_set(7, &tapping_term, sizeof(tapping_term));     // tapping term
  qmk_settings_set(25, &quick_tap_term, sizeof(quick_tap_term)); // quick tap term
  qmk_settings_set(22, &on, sizeof(on));                         // permissive hold ("balanced")
  qmk_settings_set(26, &on, sizeof(on));                         // chordal hold (opposite-hand holds)
  qmk_settings_set(27, &flow_tap_term, sizeof(flow_tap_term));   // flow tap (require-prior-idle)
}

void keyboard_post_init_keymap(void) {
  transaction_register_rpc(KM_FLASH_SYNC, flash_rpc_handler);
  if (is_keyboard_master()) {
    apply_tap_hold_defaults();
  }
}

layer_state_t layer_state_set_user(layer_state_t state) {
  return update_tri_layer_state(state, _LOWER, _RAISE, _ADJUST);
}

static bool tap_shifted(uint16_t keycode, keyrecord_t *record) {
  if (record->tap.count && record->event.pressed) {
    tap_code16(keycode);
    return false;
  }
  return true;
}

bool process_record_keymap(uint16_t keycode, keyrecord_t *record) {
  // Flash feedback for the holykeebs pointer settings (holykeebs handles the keys themselves).
  if (record->event.pressed) {
    bool setting    = g_hk_state.setting_default_sensitivity || g_hk_state.setting_sniping_sensitivity || g_hk_state.setting_scroll_throttle;
    bool peripheral = (bool)(get_mods() & MOD_MASK_SHIFT) != g_hk_state.active_is_peripheral; // as holykeebs targets it
    if (setting && keycode == KC_UP) {
      flash_half(peripheral, FLASH_UP, 150);
    } else if (setting && keycode == KC_DOWN) {
      flash_half(peripheral, FLASH_DOWN, 150);
    } else if (keycode == HK_SAVE || keycode == HK_RESET) {
      flash_half(false, FLASH_SAVED, 600);
      flash_half(true, FLASH_SAVED, 600);
    }
  }

  switch (keycode) {
    case DS_O:
      if (!record->tap.count) {
        // Held: the trackpoint (main side) scrolls until O is released, like HK_D_MODE.
        g_hk_state.main.drag_scroll = record->event.pressed;
        g_hk_state.dirty            = true;
        return false;
      }
      return true;
    case LM_PLUS: return tap_shifted(KC_PLUS, record);
    case LM_CIRC: return tap_shifted(KC_CIRC, record);
    case LM_DLR:  return tap_shifted(KC_DLR, record);
  }
  return true;
}
