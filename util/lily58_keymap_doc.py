#!/usr/bin/env python3
"""Render the Lily58 vial keymap.c into readme tables and an interactive HTML page.

- readme.md: the block between <!-- layers:start --> and <!-- layers:end --> is regenerated.
  Each key shows its action and, in small text, the printed legend of the physical keycap.
- keymap.html: the real Lily58 layout (from keyboard.json) with layer tabs and hover details.

Usage: util/lily58_keymap_doc.py [keymap_dir]
"""
import html
import json
import os
import re
import sys
from pathlib import Path

KEYMAP_DIR = Path(sys.argv[1] if len(sys.argv) > 1 else 'keyboards/holykeebs/lily58/keymaps/schlechter32')
KEYBOARD_JSON = Path(os.environ.get('QMK_FIRMWARE', '../holykeebs-vial-qmk')) / 'keyboards/holykeebs/lily58/keyboard.json'

# Printed keycap legends, in LAYOUT() order: 3 rows of 6+6, the bottom row 6 + 2 inner + 6, then 4+4 thumbs.
# Thumbs go outer to inner on the left and inner to outer on the right; ▭ is the blank 1.5u thumb.
LEGEND = [
    '∞', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '♡',
    '◇', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '⌫',
    '⇥', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '⏎',
    '⌦', 'Z', 'X', 'C', 'V', 'B', '[', ']', 'N', 'M', ',', '.', "'", '/',
    '⌃', '⌥', '↓', '▭', '▭', '↑', '‡', '▲',
]

# How to reach each layer, using the printed legends.
LAYER_INFO = {
    '_BASE': 'Default layer, LEDs show your normal animation. Small text is what the key does when held.',
    '_LOWER': 'LEDs blue. Hold the ↓ thumb (or hold F / J).',
    '_RAISE': 'LEDs green. Hold the ↑ thumb (or hold G / H).',
    '_ADJUST': 'LEDs purple. Hold the ↓ and ↑ thumbs together.',
    '_PLAIN': 'LEDs gold. Typing layer without home-row mods. Turn on with RAISE + ⌥ (left), off with ⌥ (left).',
    '_SPARE': 'Empty, free for Vial.',
}

BASIC = {
    'GRV': '`', 'MINS': '-', 'EQL': '=', 'LBRC': '[', 'RBRC': ']', 'BSLS': '\\', 'SCLN': ';', 'QUOT': "'",
    'COMM': ',', 'DOT': '.', 'SLSH': '/', 'SLASH': '/', 'GRAVE': '`', 'ESC': 'Esc', 'TAB': 'Tab',
    'ENT': 'Enter', 'BSPC': 'Bksp', 'DEL': 'Del', 'SPC': 'Space', 'LEFT': '←', 'DOWN': '↓', 'UP': '↑',
    'RGHT': '→', 'HOME': 'Home', 'END': 'End', 'PGUP': 'PgUp', 'PGDN': 'PgDn', 'RALT': 'AltGr', 'LALT': 'Alt',
    'LSFT': 'Shift', 'RSFT': 'Shift', 'LCTL': 'Ctrl', 'RCTL': 'Ctrl', 'LGUI': 'GUI', 'RGUI': 'GUI',
    'EXLM': '!', 'AT': '@', 'HASH': '#', 'DLR': '$', 'PERC': '%', 'CIRC': '^', 'AMPR': '&', 'ASTR': '*',
    'LPRN': '(', 'RPRN': ')', 'UNDS': '_', 'PLUS': '+', 'LCBR': '{', 'RCBR': '}', 'PIPE': '|', 'TILD': '~',
}
NAMED = {
    'MS_BTN1': 'Left click', 'MS_BTN2': 'Right click', 'MS_BTN3': 'Middle click',
    'QK_BOOT': 'Boot', 'QK_CLEAR_EEPROM': 'Clear EEPROM',
    'RM_TOGG': 'RGB on/off', 'RM_NEXT': 'RGB mode', 'RM_HUED': 'Hue −', 'RM_HUEU': 'Hue +',
    'RM_SATD': 'Sat −', 'RM_SATU': 'Sat +', 'RM_VALD': 'Bright −', 'RM_VALU': 'Bright +',
    'HK_SAVE': 'Save pointer', 'HK_RESET': 'Reset pointer', 'HK_DUMP': 'Dump pointer',
    'HK_P_SET_D': 'Sensitivity', 'HK_P_SET_S': 'Snipe sens.', 'HK_P_SET_THR': 'Scroll throttle',
    'HK_S_MODE': 'Snipe', 'HK_S_MODE_T': 'Snipe toggle', 'HK_D_MODE': 'Drag scroll',
    'HK_D_MODE_T': 'Drag scroll toggle', 'HK_C_SCROLL': 'Scroll lock',
}
DESCRIPTIONS = {
    'MS_BTN1': 'Mouse button 1.', 'MS_BTN2': 'Mouse button 2.', 'MS_BTN3': 'Mouse button 3.',
    'QK_BOOT': 'Reboots the half that has the USB cable into the bootloader (RPI-RP2 drive).',
    'QK_CLEAR_EEPROM': 'Wipes saved settings: Vial keymap changes, QMK Settings and pointer settings.',
    'RM_TOGG': 'LEDs on / off.', 'RM_NEXT': 'Next LED animation.',
    'RM_HUED': 'LED hue down.', 'RM_HUEU': 'LED hue up.',
    'RM_SATD': 'LED saturation down.', 'RM_SATU': 'LED saturation up.',
    'RM_VALD': 'LED brightness down (also dims the layer colours).', 'RM_VALU': 'LED brightness up.',
    'HK_SAVE': 'Saves the pointer settings so they survive a reboot.',
    'HK_RESET': 'Resets the pointer settings to the defaults.',
    'HK_DUMP': 'Prints the pointer settings to the debug console (only with CONSOLE=yes builds).',
    'HK_P_SET_D': 'Hold, then tap ↓ / ↑ to change the normal pointer sensitivity. Add Shift for the touchpad.',
    'HK_P_SET_S': 'Hold, then tap ↓ / ↑ to change the sniping (slow) sensitivity. Add Shift for the touchpad.',
    'HK_P_SET_THR': 'Hold, then tap ↓ / ↑ to change the scroll throttle (higher = slower scrolling). Add Shift '
                    'for the touchpad.',
    'HK_S_MODE': 'Slow, precise pointer while held. Add Shift for the touchpad.',
    'HK_S_MODE_T': 'Toggle slow, precise pointer. Add Shift for the touchpad.',
    'HK_D_MODE': 'Pointer movement scrolls while held. Add Shift for the touchpad.',
    'HK_D_MODE_T': 'Toggle: pointer movement scrolls. Add Shift for the touchpad.',
    'HK_C_SCROLL': 'Cycle scroll lock: off → horizontal only → vertical only.',
}
MOD_TAPS = {
    'LCTL_T': 'Ctrl', 'RCTL_T': 'Ctrl', 'LGUI_T': 'GUI', 'RGUI_T': 'GUI', 'LALT_T': 'Alt', 'RALT_T': 'AltGr',
    'LSFT_T': 'Shift', 'RSFT_T': 'Shift', 'MEH_T': 'Meh', 'C_S_T': 'Ctrl+Shift',
}
MOD_WRAPS = {'C': 'Ctrl+', 'LCTL': 'Ctrl+', 'S': 'Shift+', 'A': 'Alt+', 'G': 'GUI+'}
HOLD_NOTES = {
    'Meh': 'Meh = Ctrl+Shift+Alt.',
    'Ctrl+Shift': 'Holding it alone takes the tapping term (280 ms); pressing another key makes it a hold at once.',
}


def split_args(text):
    args, depth, cur = [], 0, ''
    for ch in text:
        if ch == ',' and depth == 0:
            args.append(cur.strip())
            cur = ''
            continue
        depth += ch == '('
        depth -= ch == ')'
        cur += ch
    if cur.strip():
        args.append(cur.strip())
    return args


def parse(src):
    src = re.sub(r'//.*', '', src)
    defines = dict(re.findall(r'^#define\s+(\w+)\s+(.+?)\s*$', src, re.M))
    layer_enum = re.search(r'enum layer_number\s*{(.*?)}', src, re.S).group(1)
    layers = re.findall(r'(_\w+)', layer_enum)
    shifted = dict(re.findall(r'case\s+(\w+):\s*return\s+tap_shifted\((\w+)', src))
    tri = re.search(r'update_tri_layer_state\(\s*state\s*,\s*(\w+)\s*,\s*(\w+)\s*,\s*(\w+)\s*\)', src)
    tri_layers = tri.groups() if tri else None
    keymaps = {}
    for m in re.finditer(r'\[(_\w+)\]\s*=\s*LAYOUT\(', src):
        depth, i = 1, m.end()
        while depth:
            depth += {'(': 1, ')': -1}.get(src[i], 0)
            i += 1
        keymaps[m.group(1)] = split_args(src[m.end():i - 1])
    return defines, layers, shifted, keymaps, tri_layers


def resolve(kc, defines):
    while kc in defines:
        kc = defines[kc]
    return kc


def describe(kc, defines, shifted):
    """Return a dict with tap, hold, description and the expanded keycode. tap is None for transparent."""
    name = kc
    if kc in shifted:
        inner = describe(resolve(kc, defines), defines, {})
        tap = describe(shifted[kc], defines, {})['tap']
        return {**inner, 'tap': tap, 'code': f'{name} = {resolve(kc, defines)}, taps {shifted[kc]}'}
    kc = resolve(kc, defines)
    code = kc if kc == name else f'{name} = {kc}'
    info = {'tap': None, 'hold': None, 'desc': '', 'code': code}
    if kc in ('_______', 'KC_TRNS', 'KC_TRANSPARENT'):
        info['desc'] = 'Transparent: does what the key does on the layer below.'
        return info
    if kc in ('XXXXXXX', 'KC_NO'):
        return {**info, 'tap': '', 'desc': 'Does nothing.'}
    if kc in NAMED:
        return {**info, 'tap': NAMED[kc], 'desc': DESCRIPTIONS.get(kc, '')}
    m = re.fullmatch(r'(\w+)\((.*)\)', kc)
    if m:
        fn, args = m.group(1), split_args(m.group(2))
        if fn in MOD_TAPS:
            hold = MOD_TAPS[fn]
            return {**info, 'tap': describe(args[0], defines, shifted)['tap'], 'hold': hold,
                    'desc': HOLD_NOTES.get(hold, '')}
        if fn == 'LT':
            return {**info, 'tap': describe(args[1], defines, shifted)['tap'], 'hold': args[0].lstrip('_'),
                    'desc': f'Hold for the {args[0].lstrip("_")} layer.'}
        if fn == 'MO':
            return {**info, 'tap': args[0].lstrip('_'), 'desc': f'Hold for the {args[0].lstrip("_")} layer.'}
        if fn == 'TO':
            return {**info, 'tap': '→ ' + args[0].lstrip('_'), 'desc': f'Switch to the {args[0].lstrip("_")} layer.'}
        if fn in MOD_WRAPS:
            return {**info, 'tap': MOD_WRAPS[fn] + describe(args[0], defines, shifted)['tap']}
    base = kc[3:] if kc.startswith('KC_') else kc
    if re.fullmatch(r'[A-Z0-9]|F\d+', base):
        return {**info, 'tap': base}
    return {**info, 'tap': BASIC.get(base, base)}


def load_layers():
    defines, layers, shifted, keymaps, tri = parse((KEYMAP_DIR / 'keymap.c').read_text())

    def active_below(layer):
        # Layers that are also active while `layer` is on, highest first: the tri-layer keeps its two
        # source layers on; everything else only has the default layer underneath.
        below = [tri[1], tri[0]] if tri and layer == tri[2] else []
        return [b for b in below if b != layer] + ([layers[0]] if layer != layers[0] else [])

    result = []
    for layer in layers:
        keys = keymaps.get(layer)
        if keys is None:
            continue
        if len(keys) != len(LEGEND):
            sys.exit(f'{layer}: expected {len(LEGEND)} keys, got {len(keys)}')
        infos = [describe(k, defines, shifted) for k in keys]
        if layer != layers[0] and all(i['tap'] is None for i in infos):
            continue  # skip empty layers
        result.append({'id': layer, 'name': layer.lstrip('_'), 'info': LAYER_INFO.get(layer, ''), 'keys': infos,
                       'below': active_below(layer)})
    return result


# --- readme ---------------------------------------------------------------------------------------------------


def md_cell(key, legend, base):
    esc = html.escape
    if base:
        body = f'<b>{esc(key["tap"])}</b>' if key['tap'] else ''
        small = esc(key['hold']) if key['hold'] else ''
    else:
        body = '' if key['tap'] is None else (f'<b>{esc(key["tap"])}</b>' if key['tap'] else '·')
        if key['hold']:
            body += f'<br>{esc(key["hold"])}'
        small = f'<kbd>{esc(legend)}</kbd>'
    if small:
        body = f'{body}<br><sub>{small}</sub>' if body else f'<sub>{small}</sub>'
    return f'<td align="center">{body}</td>'


def md_table(keys, base):
    def c(i):
        return md_cell(keys[i], LEGEND[i], base)

    blank, gap = '<td></td>', '<td>&nbsp;&nbsp;&nbsp;&nbsp;</td>'
    rows = []
    for r in range(3):
        rows.append(''.join(c(r * 12 + i) for i in range(6)) + blank + gap + blank
                    + ''.join(c(r * 12 + 6 + i) for i in range(6)))
    rows.append(''.join(c(36 + i) for i in range(6)) + c(42) + gap + c(43) + ''.join(c(44 + i) for i in range(6)))
    rows.append(blank * 3 + ''.join(c(50 + i) for i in range(4)) + gap + ''.join(c(54 + i) for i in range(4))
                + blank * 3)
    return '<table>\n' + '\n'.join(f'<tr>{r}</tr>' for r in rows) + '\n</table>'


def write_readme(layers):
    parts = []
    for n, layer in enumerate(layers):
        parts.append(f'### {layer["name"]}\n\n{layer["info"]}\n\n{md_table(layer["keys"], n == 0)}\n')
    block = '\n'.join(parts)
    path = KEYMAP_DIR / 'readme.md'
    text = path.read_text()
    new, count = re.subn(r'(<!-- layers:start -->\n).*?(<!-- layers:end -->)',
                         lambda m: m.group(1) + block + m.group(2), text, flags=re.S)
    if not count:
        sys.exit('readme.md has no <!-- layers:start --> / <!-- layers:end --> markers')
    path.write_text(new)


# --- html -----------------------------------------------------------------------------------------------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Lily58 keymap</title>
<style>
  :root { --u: 64px; --bg: #1b1410; --cap: #8a5a3c; --cap-dark: #4a3a33; --legend: #ff9a3c; --text: #f3e6da; }
  body { background: var(--bg); color: var(--text); font: 15px/1.4 system-ui, sans-serif; margin: 24px; }
  h1 { font-size: 20px; margin: 0 0 12px; }
  .tabs button { background: var(--cap-dark); color: var(--text); border: 0; border-radius: 6px; padding: 6px 14px;
                 margin: 0 6px 6px 0; font-size: 14px; cursor: pointer; }
  .tabs button.active { background: var(--legend); color: #1b1410; font-weight: 600; }
  #info { margin: 6px 0 18px; opacity: .85; min-height: 1.4em; }
  #board { position: relative; height: calc(var(--u) * 6); width: calc(var(--u) * 16.6); }
  .key { position: absolute; box-sizing: border-box; padding: 4px; border-radius: 8px; background: var(--cap);
         box-shadow: inset 0 -4px 0 rgba(0,0,0,.35); display: flex; flex-direction: column; justify-content: center;
         align-items: center; text-align: center; cursor: default; overflow: hidden; }
  .key.mod { background: var(--cap-dark); }
  .key.trans { opacity: .4; }
  .key.none { opacity: .25; }
  .key:hover { outline: 2px solid var(--legend); opacity: 1; }
  .key .tap { font-weight: 600; font-size: 13px; line-height: 1.1; }
  .key .hold { font-size: 10px; color: var(--legend); margin-top: 2px; }
  .key .legend { position: absolute; left: 5px; top: 3px; font-size: 12px; color: var(--legend); opacity: .9; }
  #tip { position: fixed; pointer-events: none; background: #2a201a; border: 1px solid var(--legend); border-radius: 6px;
         padding: 8px 10px; max-width: 320px; font-size: 13px; display: none; z-index: 10; }
  #tip code { color: var(--legend); font-size: 12px; }
  .hint { margin-top: 16px; opacity: .7; font-size: 13px; }
</style>
</head>
<body>
<h1>Lily58 keymap: trackpoint left, TPS43 touchpad right</h1>
<div class="tabs" id="tabs"></div>
<div id="info"></div>
<div id="board"></div>
<div id="tip"></div>
<p class="hint">Orange corner text is the printed keycap legend. Hover a key for details; press 1–9 to switch layers.
Faded keys are transparent and show what they inherit from the layer below.
Generated from keymap.c by util/lily58_keymap_doc.py.</p>
<script>
const LAYERS = __LAYERS__;
const GEOMETRY = __GEOMETRY__;
const LEGEND = __LEGEND__;
const MODS = new Set(['∞','◇','⇥','⌦','♡','⌫','⏎','⌃','⌥','↓','↑','‡','▲','▭']);
const board = document.getElementById('board'), tip = document.getElementById('tip');
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

function effective(layerIdx, i) {
  // Transparent keys fall through to the highest other active layer that defines the key.
  for (const id of LAYERS[layerIdx].below) {
    const l = LAYERS.find(x => x.id === id);
    if (l && l.keys[i].tap !== null) return l.keys[i];
  }
  return null;
}

function render(idx) {
  const layer = LAYERS[idx];
  document.querySelectorAll('.tabs button').forEach((b, j) => b.classList.toggle('active', j === idx));
  document.getElementById('info').textContent = layer.info;
  history.replaceState(null, '', '#' + layer.name.toLowerCase());
  board.innerHTML = '';
  layer.keys.forEach((key, i) => {
    const g = GEOMETRY[i], el = document.createElement('div');
    let shown = key, cls = '';
    if (key.tap === null) { shown = effective(idx, i) || key; cls = 'trans'; }
    else if (key.tap === '') { cls = 'none'; }
    el.className = 'key ' + cls + (MODS.has(LEGEND[i]) ? ' mod' : '');
    Object.assign(el.style, { left: `calc(var(--u) * ${g.x})`, top: `calc(var(--u) * ${g.y})`,
      width: `calc(var(--u) * ${g.w} - 4px)`, height: `calc(var(--u) * ${g.h} - 4px)` });
    el.innerHTML = `<span class="legend">${esc(LEGEND[i])}</span>` +
      `<span class="tap">${esc(shown.tap || '')}</span>` +
      (shown.hold ? `<span class="hold">hold: ${esc(shown.hold)}</span>` : '');
    el.addEventListener('mousemove', e => showTip(e, idx, i));
    el.addEventListener('mouseleave', () => tip.style.display = 'none');
    board.appendChild(el);
  });
}

function showTip(e, idx, i) {
  const key = LAYERS[idx].keys[i];
  const lines = [`<b>Key ${esc(LEGEND[i])}</b> on ${esc(LAYERS[idx].name)}`];
  if (key.tap === null) {
    const inh = effective(idx, i);
    lines.push('Transparent' + (inh ? `: acts as <b>${esc(inh.tap)}</b>` + (inh.hold ? ` / hold ${esc(inh.hold)}` : '') : ''));
  } else {
    if (key.tap) lines.push(`Tap: <b>${esc(key.tap)}</b>`);
    if (key.hold) lines.push(`Hold: <b>${esc(key.hold)}</b>`);
    if (key.desc) lines.push(esc(key.desc));
  }
  lines.push(`<code>${esc(key.code)}</code>`);
  tip.innerHTML = lines.join('<br>');
  tip.style.display = 'block';
  const x = Math.min(e.clientX + 14, window.innerWidth - tip.offsetWidth - 8);
  tip.style.left = x + 'px';
  tip.style.top = (e.clientY + 14) + 'px';
}

const tabs = document.getElementById('tabs');
LAYERS.forEach((l, j) => {
  const b = document.createElement('button');
  b.textContent = `${j + 1} ${l.name}`;
  b.onclick = () => render(j);
  tabs.appendChild(b);
});
document.addEventListener('keydown', e => {
  const n = parseInt(e.key, 10);
  if (n >= 1 && n <= LAYERS.length) render(n - 1);
});
const start = LAYERS.findIndex(l => '#' + l.name.toLowerCase() === location.hash);
render(start < 0 ? 0 : start);
</script>
</body>
</html>
"""


def write_html(layers):
    layout = json.loads(KEYBOARD_JSON.read_text())['layouts']['LAYOUT']['layout']
    geometry = [{'x': k['x'], 'y': k['y'], 'w': k.get('w', 1), 'h': k.get('h', 1)} for k in layout]
    page = (HTML_TEMPLATE.replace('__LAYERS__', json.dumps(layers, ensure_ascii=False))
            .replace('__GEOMETRY__', json.dumps(geometry))
            .replace('__LEGEND__', json.dumps(LEGEND, ensure_ascii=False)))
    (KEYMAP_DIR / 'keymap.html').write_text(page)


def main():
    layers = load_layers()
    write_readme(layers)
    write_html(layers)


if __name__ == '__main__':
    main()
