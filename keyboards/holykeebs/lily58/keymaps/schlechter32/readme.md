# holykeebs Lily58 Vial keymap: trackpoint (left) + TPS43 touchpad (right)

A port of my ZMK Corne layout ([`zmk-config/config/corne.keymap`](https://github.com/schlechter32/zmk-config)) to the Lily58.
The keys the Corne doesn't have (the number row, the two inner keys and the outer thumbs) are used for extras.
The source is [`keymap.c`](keymap.c).

**Interactive version:** [`keymap.html`](keymap.html). Open it locally in a browser (`xdg-open keyboards/holykeebs/lily58/keymaps/schlechter32/keymap.html`) for the real board shape, layer tabs and hover details.

## Layers

Big text is what the key does. Small <kbd>text</kbd> is the printed legend on the keycap (▭ = the blank wide thumb key).
On BASE the small text is the hold action instead. Empty keys fall through to the layer below.

<!-- Generated from keymap.c by util/lily58_keymap_doc.py; edit keymap.c and rerun it (util/flash_lily58.sh --build does). -->
<!-- layers:start -->
### BASE

Default layer, LEDs show your normal animation. Small text is what the key does when held.

<table>
<tr><td align="center"><b>`</b></td><td align="center"><b>1</b></td><td align="center"><b>2</b></td><td align="center"><b>3</b></td><td align="center"><b>4</b></td><td align="center"><b>5</b></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>6</b></td><td align="center"><b>7</b></td><td align="center"><b>8</b></td><td align="center"><b>9</b></td><td align="center"><b>0</b></td><td align="center"><b>-</b></td></tr>
<tr><td align="center"><b>Esc</b></td><td align="center"><b>Q</b></td><td align="center"><b>W</b></td><td align="center"><b>E</b></td><td align="center"><b>R</b></td><td align="center"><b>T</b></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>Y</b></td><td align="center"><b>U</b></td><td align="center"><b>I</b></td><td align="center"><b>O</b><br><sub>Drag scroll</sub></td><td align="center"><b>P</b></td><td align="center"><b>Bksp</b></td></tr>
<tr><td align="center"><b>Tab</b><br><sub>Shift</sub></td><td align="center"><b>A</b><br><sub>Ctrl</sub></td><td align="center"><b>S</b><br><sub>GUI</sub></td><td align="center"><b>D</b><br><sub>Alt</sub></td><td align="center"><b>F</b><br><sub>LOWER</sub></td><td align="center"><b>G</b><br><sub>RAISE</sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>H</b><br><sub>RAISE</sub></td><td align="center"><b>J</b><br><sub>LOWER</sub></td><td align="center"><b>K</b><br><sub>Alt</sub></td><td align="center"><b>L</b><br><sub>GUI</sub></td><td align="center"><b>;</b><br><sub>Ctrl</sub></td><td align="center"><b>Enter</b><br><sub>Shift</sub></td></tr>
<tr><td align="center"><b>Del</b></td><td align="center"><b>Z</b></td><td align="center"><b>X</b></td><td align="center"><b>C</b></td><td align="center"><b>V</b></td><td align="center"><b>B</b></td><td align="center"><b>[</b><br><sub>Ctrl+Shift</sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><b>]</b><br><sub>Ctrl+Shift</sub></td><td align="center"><b>N</b></td><td align="center"><b>M</b></td><td align="center"><b>,</b></td><td align="center"><b>.</b></td><td align="center"><b>&#x27;</b></td><td align="center"><b>/</b><br><sub>Meh</sub></td></tr>
<tr><td></td><td></td><td></td><td align="center"><b>Left click</b></td><td align="center"><b>AltGr</b></td><td align="center"><b>LOWER</b></td><td align="center"><b>Space</b><br><sub>Meh</sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><b>Ctrl+Bksp</b></td><td align="center"><b>RAISE</b></td><td align="center"><b>AltGr</b></td><td align="center"><b>Right click</b></td><td></td><td></td><td></td></tr>
</table>

### LOWER

LEDs blue. Hold the ↓ thumb (or hold F / J).

<table>
<tr><td align="center"><sub><kbd>∞</kbd></sub></td><td align="center"><sub><kbd>1</kbd></sub></td><td align="center"><sub><kbd>2</kbd></sub></td><td align="center"><sub><kbd>3</kbd></sub></td><td align="center"><sub><kbd>4</kbd></sub></td><td align="center"><sub><kbd>5</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><sub><kbd>6</kbd></sub></td><td align="center"><sub><kbd>7</kbd></sub></td><td align="center"><sub><kbd>8</kbd></sub></td><td align="center"><sub><kbd>9</kbd></sub></td><td align="center"><sub><kbd>0</kbd></sub></td><td align="center"><sub><kbd>♡</kbd></sub></td></tr>
<tr><td align="center"><b>F1</b><br><sub><kbd>◇</kbd></sub></td><td align="center"><b>F2</b><br><sub><kbd>Q</kbd></sub></td><td align="center"><b>F3</b><br><sub><kbd>W</kbd></sub></td><td align="center"><b>F4</b><br><sub><kbd>E</kbd></sub></td><td align="center"><b>F5</b><br><sub><kbd>R</kbd></sub></td><td align="center"><b>F6</b><br><sub><kbd>T</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>F7</b><br><sub><kbd>Y</kbd></sub></td><td align="center"><b>F8</b><br><sub><kbd>U</kbd></sub></td><td align="center"><b>F9</b><br><sub><kbd>I</kbd></sub></td><td align="center"><b>F10</b><br><sub><kbd>O</kbd></sub></td><td align="center"><b>F11</b><br><sub><kbd>P</kbd></sub></td><td align="center"><b>F12</b><br><sub><kbd>⌫</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>⇥</kbd></sub></td><td align="center"><b>_</b><br><sub><kbd>A</kbd></sub></td><td align="center"><b>+</b><br>Ctrl<br><sub><kbd>S</kbd></sub></td><td align="center"><b>^</b><br>Alt<br><sub><kbd>D</kbd></sub></td><td align="center"><b>$</b><br>GUI<br><sub><kbd>F</kbd></sub></td><td align="center"><sub><kbd>G</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>←</b><br><sub><kbd>H</kbd></sub></td><td align="center"><b>↓</b><br><sub><kbd>J</kbd></sub></td><td align="center"><b>↑</b><br><sub><kbd>K</kbd></sub></td><td align="center"><b>→</b><br><sub><kbd>L</kbd></sub></td><td align="center"><b>End</b><br><sub><kbd>;</kbd></sub></td><td align="center"><sub><kbd>⏎</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>⌦</kbd></sub></td><td align="center"><b>~</b><br><sub><kbd>Z</kbd></sub></td><td align="center"><b>Drag scroll</b><br><sub><kbd>X</kbd></sub></td><td align="center"><b>Middle click</b><br><sub><kbd>C</kbd></sub></td><td align="center"><b>Snipe</b><br><sub><kbd>V</kbd></sub></td><td align="center"><b>F11</b><br><sub><kbd>B</kbd></sub></td><td align="center"><sub><kbd>[</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><sub><kbd>]</kbd></sub></td><td align="center"><b>Home</b><br><sub><kbd>N</kbd></sub></td><td align="center"><b>PgDn</b><br><sub><kbd>M</kbd></sub></td><td align="center"><b>PgUp</b><br><sub><kbd>,</kbd></sub></td><td align="center"><b>End</b><br><sub><kbd>.</kbd></sub></td><td align="center"><b>PgUp</b><br><sub><kbd>&#x27;</kbd></sub></td><td align="center"><sub><kbd>/</kbd></sub></td></tr>
<tr><td></td><td></td><td></td><td align="center"><sub><kbd>⌃</kbd></sub></td><td align="center"><sub><kbd>⌥</kbd></sub></td><td align="center"><sub><kbd>↓</kbd></sub></td><td align="center"><sub><kbd>▭</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><sub><kbd>▭</kbd></sub></td><td align="center"><sub><kbd>↑</kbd></sub></td><td align="center"><sub><kbd>‡</kbd></sub></td><td align="center"><sub><kbd>▲</kbd></sub></td><td></td><td></td><td></td></tr>
</table>

### RAISE

LEDs green. Hold the ↑ thumb (or hold G / H).

<table>
<tr><td align="center"><sub><kbd>∞</kbd></sub></td><td align="center"><sub><kbd>1</kbd></sub></td><td align="center"><sub><kbd>2</kbd></sub></td><td align="center"><sub><kbd>3</kbd></sub></td><td align="center"><sub><kbd>4</kbd></sub></td><td align="center"><sub><kbd>5</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><sub><kbd>6</kbd></sub></td><td align="center"><sub><kbd>7</kbd></sub></td><td align="center"><sub><kbd>8</kbd></sub></td><td align="center"><sub><kbd>9</kbd></sub></td><td align="center"><sub><kbd>0</kbd></sub></td><td align="center"><sub><kbd>♡</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>◇</kbd></sub></td><td align="center"><b>@</b><br><sub><kbd>Q</kbd></sub></td><td align="center"><b>!</b><br><sub><kbd>W</kbd></sub></td><td align="center"><b>{</b><br><sub><kbd>E</kbd></sub></td><td align="center"><b>}</b><br><sub><kbd>R</kbd></sub></td><td align="center"><b>&amp;</b><br><sub><kbd>T</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>^</b><br><sub><kbd>Y</kbd></sub></td><td align="center"><b>7</b><br><sub><kbd>U</kbd></sub></td><td align="center"><b>8</b><br><sub><kbd>I</kbd></sub></td><td align="center"><b>9</b><br><sub><kbd>O</kbd></sub></td><td align="center"><b>$</b><br><sub><kbd>P</kbd></sub></td><td align="center"><sub><kbd>⌫</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>⇥</kbd></sub></td><td align="center"><b>-</b><br><sub><kbd>A</kbd></sub></td><td align="center"><b>\</b><br><sub><kbd>S</kbd></sub></td><td align="center"><b>(</b><br><sub><kbd>D</kbd></sub></td><td align="center"><b>)</b><br><sub><kbd>F</kbd></sub></td><td align="center"><b>*</b><br><sub><kbd>G</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>0</b><br><sub><kbd>H</kbd></sub></td><td align="center"><b>4</b><br><sub><kbd>J</kbd></sub></td><td align="center"><b>5</b><br><sub><kbd>K</kbd></sub></td><td align="center"><b>6</b><br><sub><kbd>L</kbd></sub></td><td align="center"><b>=</b><br><sub><kbd>;</kbd></sub></td><td align="center"><sub><kbd>⏎</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>⌦</kbd></sub></td><td align="center"><b>`</b><br><sub><kbd>Z</kbd></sub></td><td align="center"><b>#</b><br><sub><kbd>X</kbd></sub></td><td align="center"><b>[</b><br><sub><kbd>C</kbd></sub></td><td align="center"><b>]</b><br><sub><kbd>V</kbd></sub></td><td align="center"><b>%</b><br><sub><kbd>B</kbd></sub></td><td align="center"><sub><kbd>[</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><sub><kbd>]</kbd></sub></td><td align="center"><b>|</b><br><sub><kbd>N</kbd></sub></td><td align="center"><b>1</b><br><sub><kbd>M</kbd></sub></td><td align="center"><b>2</b><br><sub><kbd>,</kbd></sub></td><td align="center"><b>3</b><br><sub><kbd>.</kbd></sub></td><td align="center"><b>,</b><br><sub><kbd>&#x27;</kbd></sub></td><td align="center"><sub><kbd>/</kbd></sub></td></tr>
<tr><td></td><td></td><td></td><td align="center"><sub><kbd>⌃</kbd></sub></td><td align="center"><b>→ PLAIN</b><br><sub><kbd>⌥</kbd></sub></td><td align="center"><sub><kbd>↓</kbd></sub></td><td align="center"><sub><kbd>▭</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><sub><kbd>▭</kbd></sub></td><td align="center"><sub><kbd>↑</kbd></sub></td><td align="center"><sub><kbd>‡</kbd></sub></td><td align="center"><sub><kbd>▲</kbd></sub></td><td></td><td></td><td></td></tr>
</table>

### ADJUST

LEDs purple. Hold the ↓ and ↑ thumbs together.

<table>
<tr><td align="center"><b>Clear EEPROM</b><br><sub><kbd>∞</kbd></sub></td><td align="center">·<br><sub><kbd>1</kbd></sub></td><td align="center">·<br><sub><kbd>2</kbd></sub></td><td align="center">·<br><sub><kbd>3</kbd></sub></td><td align="center">·<br><sub><kbd>4</kbd></sub></td><td align="center">·<br><sub><kbd>5</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center">·<br><sub><kbd>6</kbd></sub></td><td align="center">·<br><sub><kbd>7</kbd></sub></td><td align="center">·<br><sub><kbd>8</kbd></sub></td><td align="center">·<br><sub><kbd>9</kbd></sub></td><td align="center">·<br><sub><kbd>0</kbd></sub></td><td align="center">·<br><sub><kbd>♡</kbd></sub></td></tr>
<tr><td align="center"><b>Boot</b><br><sub><kbd>◇</kbd></sub></td><td align="center"><b>RGB on/off</b><br><sub><kbd>Q</kbd></sub></td><td align="center"><b>RGB mode</b><br><sub><kbd>W</kbd></sub></td><td align="center"><b>Hue −</b><br><sub><kbd>E</kbd></sub></td><td align="center"><b>Hue +</b><br><sub><kbd>R</kbd></sub></td><td align="center"><b>Scroll lock</b><br><sub><kbd>T</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center">·<br><sub><kbd>Y</kbd></sub></td><td align="center">·<br><sub><kbd>U</kbd></sub></td><td align="center">·<br><sub><kbd>I</kbd></sub></td><td align="center">·<br><sub><kbd>O</kbd></sub></td><td align="center">·<br><sub><kbd>P</kbd></sub></td><td align="center"><b>Boot</b><br><sub><kbd>⌫</kbd></sub></td></tr>
<tr><td align="center">·<br><sub><kbd>⇥</kbd></sub></td><td align="center"><b>Sensitivity</b><br><sub><kbd>A</kbd></sub></td><td align="center"><b>Snipe sens.</b><br><sub><kbd>S</kbd></sub></td><td align="center"><b>Scroll throttle</b><br><sub><kbd>D</kbd></sub></td><td align="center"><b>Save pointer</b><br><sub><kbd>F</kbd></sub></td><td align="center"><b>Snipe toggle</b><br><sub><kbd>G</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center">·<br><sub><kbd>H</kbd></sub></td><td align="center"><b>↓</b><br><sub><kbd>J</kbd></sub></td><td align="center"><b>↑</b><br><sub><kbd>K</kbd></sub></td><td align="center">·<br><sub><kbd>L</kbd></sub></td><td align="center">·<br><sub><kbd>;</kbd></sub></td><td align="center">·<br><sub><kbd>⏎</kbd></sub></td></tr>
<tr><td align="center"><b>Shift</b><br><sub><kbd>⌦</kbd></sub></td><td align="center"><b>Bright −</b><br><sub><kbd>Z</kbd></sub></td><td align="center"><b>Bright +</b><br><sub><kbd>X</kbd></sub></td><td align="center"><b>Sat −</b><br><sub><kbd>C</kbd></sub></td><td align="center"><b>Sat +</b><br><sub><kbd>V</kbd></sub></td><td align="center"><b>Drag scroll toggle</b><br><sub><kbd>B</kbd></sub></td><td align="center">·<br><sub><kbd>[</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center">·<br><sub><kbd>]</kbd></sub></td><td align="center">·<br><sub><kbd>N</kbd></sub></td><td align="center">·<br><sub><kbd>M</kbd></sub></td><td align="center">·<br><sub><kbd>,</kbd></sub></td><td align="center"><b>Reset pointer</b><br><sub><kbd>.</kbd></sub></td><td align="center"><b>Dump pointer</b><br><sub><kbd>&#x27;</kbd></sub></td><td align="center">·<br><sub><kbd>/</kbd></sub></td></tr>
<tr><td></td><td></td><td></td><td align="center"><sub><kbd>⌃</kbd></sub></td><td align="center"><sub><kbd>⌥</kbd></sub></td><td align="center"><sub><kbd>↓</kbd></sub></td><td align="center"><sub><kbd>▭</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><sub><kbd>▭</kbd></sub></td><td align="center"><sub><kbd>↑</kbd></sub></td><td align="center"><sub><kbd>‡</kbd></sub></td><td align="center"><sub><kbd>▲</kbd></sub></td><td></td><td></td><td></td></tr>
</table>

### PLAIN

LEDs gold. Typing layer without home-row mods. Turn on with RAISE + ⌥ (left), off with ⌥ (left).

<table>
<tr><td align="center"><sub><kbd>∞</kbd></sub></td><td align="center"><sub><kbd>1</kbd></sub></td><td align="center"><sub><kbd>2</kbd></sub></td><td align="center"><sub><kbd>3</kbd></sub></td><td align="center"><sub><kbd>4</kbd></sub></td><td align="center"><sub><kbd>5</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><sub><kbd>6</kbd></sub></td><td align="center"><sub><kbd>7</kbd></sub></td><td align="center"><sub><kbd>8</kbd></sub></td><td align="center"><sub><kbd>9</kbd></sub></td><td align="center"><sub><kbd>0</kbd></sub></td><td align="center"><sub><kbd>♡</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>◇</kbd></sub></td><td align="center"><b>Q</b><br><sub><kbd>Q</kbd></sub></td><td align="center"><b>W</b><br><sub><kbd>W</kbd></sub></td><td align="center"><b>E</b><br><sub><kbd>E</kbd></sub></td><td align="center"><b>R</b><br><sub><kbd>R</kbd></sub></td><td align="center"><b>T</b><br><sub><kbd>T</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>Y</b><br><sub><kbd>Y</kbd></sub></td><td align="center"><b>U</b><br><sub><kbd>U</kbd></sub></td><td align="center"><b>I</b><br><sub><kbd>I</kbd></sub></td><td align="center"><b>O</b><br><sub><kbd>O</kbd></sub></td><td align="center"><b>P</b><br><sub><kbd>P</kbd></sub></td><td align="center"><sub><kbd>⌫</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>⇥</kbd></sub></td><td align="center"><b>A</b><br><sub><kbd>A</kbd></sub></td><td align="center"><b>S</b><br><sub><kbd>S</kbd></sub></td><td align="center"><b>D</b><br><sub><kbd>D</kbd></sub></td><td align="center"><b>F</b><br><sub><kbd>F</kbd></sub></td><td align="center"><b>G</b><br><sub><kbd>G</kbd></sub></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td></td><td align="center"><b>H</b><br><sub><kbd>H</kbd></sub></td><td align="center"><b>J</b><br><sub><kbd>J</kbd></sub></td><td align="center"><b>K</b><br><sub><kbd>K</kbd></sub></td><td align="center"><b>L</b><br><sub><kbd>L</kbd></sub></td><td align="center"><b>;</b><br><sub><kbd>;</kbd></sub></td><td align="center"><sub><kbd>⏎</kbd></sub></td></tr>
<tr><td align="center"><sub><kbd>⌦</kbd></sub></td><td align="center"><b>Z</b><br><sub><kbd>Z</kbd></sub></td><td align="center"><b>X</b><br><sub><kbd>X</kbd></sub></td><td align="center"><b>C</b><br><sub><kbd>C</kbd></sub></td><td align="center"><b>V</b><br><sub><kbd>V</kbd></sub></td><td align="center"><b>B</b><br><sub><kbd>B</kbd></sub></td><td align="center"><sub><kbd>[</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><sub><kbd>]</kbd></sub></td><td align="center"><b>N</b><br><sub><kbd>N</kbd></sub></td><td align="center"><b>M</b><br><sub><kbd>M</kbd></sub></td><td align="center"><b>,</b><br><sub><kbd>,</kbd></sub></td><td align="center"><b>.</b><br><sub><kbd>.</kbd></sub></td><td align="center"><b>&#x27;</b><br><sub><kbd>&#x27;</kbd></sub></td><td align="center"><sub><kbd>/</kbd></sub></td></tr>
<tr><td></td><td></td><td></td><td align="center"><sub><kbd>⌃</kbd></sub></td><td align="center"><b>→ BASE</b><br><sub><kbd>⌥</kbd></sub></td><td align="center"><sub><kbd>↓</kbd></sub></td><td align="center"><sub><kbd>▭</kbd></sub></td><td>&nbsp;&nbsp;&nbsp;&nbsp;</td><td align="center"><sub><kbd>▭</kbd></sub></td><td align="center"><sub><kbd>↑</kbd></sub></td><td align="center"><sub><kbd>‡</kbd></sub></td><td align="center"><sub><kbd>▲</kbd></sub></td><td></td><td></td><td></td></tr>
</table>
<!-- layers:end -->

### Notes

- **Home-row mods:** Ctrl / GUI / Alt on A S D and K L ;. Layer-taps on F G H J (LOWER / RAISE).
- **Inner keys** <kbd>[</kbd> <kbd>]</kbd>: tap for `[` / `]`, hold for Ctrl+Shift, so the left pinky doesn't have to hold both Ctrl (A) and Shift (⇥).
  They work with keys on either hand. Holding one alone, e.g. for Ctrl+Shift+click, takes the 280 ms tapping term.
- **Meh** is Ctrl+Shift+Alt.
- **Hold <kbd>O</kbd>** to scroll with the trackpoint (drag-scroll) until you let go. It kicks in after the 280 ms tapping term, or as soon as you press another key; while typing, Flow Tap keeps it a plain `o`.
- **LED colours:** all 35 LEDs per half (per-key + underglow) take the layer colour: LOWER blue, RAISE green, ADJUST purple, PLAIN gold. BASE shows your normal animation (change it in Vial → Lighting or with *RGB mode* on ADJUST). With RGB switched off, the layer colours are off too.

## Pointer settings, step by step

All of these are on ADJUST: keep the <kbd>↓</kbd> and <kbd>↑</kbd> thumbs held the whole time.

| To change | Hold | Then tap |
|---|---|---|
| Trackpoint speed | <kbd>A</kbd> (Sensitivity) | <kbd>J</kbd> slower, <kbd>K</kbd> faster |
| Trackpoint sniping speed | <kbd>S</kbd> (Snipe sens.) | <kbd>J</kbd> / <kbd>K</kbd> |
| Trackpoint scroll speed | <kbd>D</kbd> (Scroll throttle) | <kbd>J</kbd> / <kbd>K</kbd> (higher throttle = slower scrolling) |
| Touchpad, any of the above | <kbd>⌦</kbd> (Shift) **and** <kbd>A</kbd> / <kbd>S</kbd> / <kbd>D</kbd> | <kbd>J</kbd> / <kbd>K</kbd> |

Each tap changes the value by a small step (speed ±0.1; the trackpoint starts at 2.0, so about 5 % per tap). Tap 5–10 times to feel a difference.
The LEDs confirm every step on the half whose device changed: **white flash = up, red flash = down** (left half = trackpoint, right half = touchpad).
No flash means the key combination didn't register as an adjustment.

Then tap <kbd>F</kbd> (Save pointer), still on ADJUST, or the change is lost at the next reboot. Saving flashes all LEDs cyan.
<kbd>B</kbd> toggles drag-scroll and <kbd>G</kbd> toggles sniping (add <kbd>⌦</kbd> for the touchpad); <kbd>T</kbd> cycles scroll lock.
On LOWER you can also hold <kbd>X</kbd> to scroll with the trackpoint and hold <kbd>V</kbd> for slow sniping.

## Tap-hold behaviour

| Setting | Value | ZMK equivalent |
|---|---|---|
| Tapping term | 280 ms (one value for all keys) | `tapping-term-ms` |
| Quick tap term | 175 ms | `quick-tap-ms` |
| Permissive hold | on | `flavor = "balanced"` |
| Chordal hold | on, thumbs and inner keys count for both hands | `hold-trigger-key-positions` |
| Flow tap | 150 ms (letters, space, `;` `/`) | `require-prior-idle-ms` |

All of these are QMK Settings in Vial and can be changed there. After a flash they start out all off, so the
keymap applies the values above once at startup. Flashing also resets keymap changes made in Vial;
`keymap.c` is the source of truth.

## Build and flash

This keymap lives in a fork of [holykeebs/qmk-userspace](https://github.com/holykeebs/qmk-userspace) and builds
against [holykeebs/vial-qmk](https://github.com/holykeebs/vial-qmk) (branch `hk-master`), checked out next to it:

```sh
git clone --recurse-submodules -b hk-master https://github.com/holykeebs/vial-qmk.git ../holykeebs-vial-qmk
util/flash_lily58.sh --build   # build both halves (and these docs), then flash them one after the other
util/flash_lily58.sh           # flash the existing build
```

Keep the TRRS cable connected. Only plug or unplug TRRS when no USB cable is connected.

- *Boot* is on ADJUST at Esc (left) and Backspace (right). Either one reboots **the half that has the USB cable** into the bootloader.
- **Left half** (the USB side): LOWER + RAISE + *Boot*. No unplugging needed.
- **Right half:** move the USB cable to the right half, then LOWER + RAISE + *Boot* (or double-tap its reset button).
  Never connect USB to both halves at once while TRRS is connected.
  The keymap only runs on the left half, so **keymap-only changes just need the left half flashed**; answer `n` for the right one.
  Reflash both halves when `config.h`, `rules.mk` or the userspace changes.
