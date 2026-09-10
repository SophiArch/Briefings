#!/usr/bin/env python3
"""Generate a side-by-side layered VM-vs-Docker comparison SVG (dracula palette).

Run from anywhere: `python3 gen_diag_vm_vs_docker.py`
Regenerates diag_vm_vs_docker.svg in this same Images/ folder.
"""

import os

# ---- layout constants ----
COL_W = 220
COL_GAP = 12
N_COLS = 3
STACK_W = N_COLS * COL_W + (N_COLS - 1) * COL_GAP  # 684

ROW_H = 88
STACK_GAP = 110  # space between the two stacks
MARGIN = 40
TITLE_H = 56

BG = "#282a36"
TXT = "#f8f8f2"

# colour per layer role
C_APP = "#50fa7b"
C_BINS = "#f1fa8c"
C_GUEST_OS = "#f8f8f2"
C_ENGINE = "#8be9fd"
C_HOST = "#ff79c6"
C_INFRA = "#bd93f9"

FILL = "#3a3d4d"


def rect(x, y, w, h, stroke, label, sub=None, fill=FILL, font=22):
    lines = [f'  <rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="8" '
             f'fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>']
    cx = x + w / 2
    if sub:
        cy1 = y + h / 2 - 12
        cy2 = y + h / 2 + 16
        lines.append(f'  <text x="{cx:.1f}" y="{cy1:.1f}" fill="{TXT}" font-size="{font}" '
                      f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle">{label}</text>')
        lines.append(f'  <text x="{cx:.1f}" y="{cy2:.1f}" fill="{TXT}" font-size="{font-6}" '
                      f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle" opacity="0.8">{sub}</text>')
    else:
        cy = y + h / 2 + font * 0.35
        lines.append(f'  <text x="{cx:.1f}" y="{cy:.1f}" fill="{TXT}" font-size="{font}" '
                      f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle">{label}</text>')
    return "\n".join(lines)


def full_row(x0, y, label, stroke, sub=None, fill=FILL, font=24):
    return rect(x0, y, STACK_W, ROW_H, stroke, label, sub, fill, font)


def split_row(x0, y, labels, stroke, fill=FILL, font=22):
    parts = []
    for i, lab in enumerate(labels):
        x = x0 + i * (COL_W + COL_GAP)
        parts.append(rect(x, y, COL_W, ROW_H, stroke, lab, fill=fill, font=font))
    return "\n".join(parts)


def stack_title(x0, y, text):
    cx = x0 + STACK_W / 2
    return (f'  <text x="{cx:.1f}" y="{y:.1f}" fill="{TXT}" font-size="30" '
            f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle" font-weight="700">{text}</text>')


# ---- rows, bottom to top ----
# VM stack (6 rows) — Infra, Host OS, Hypervisor, Guest OS x3, Bin/Libs x3, App x3
vm_rows = [
    ("full", "Infrastructure", C_INFRA, None),
    ("full", "Host Operating System", C_HOST, None),
    ("full", "Hypervisor", C_ENGINE, None),
    ("split", ["Guest OS", "Guest OS", "Guest OS"], C_GUEST_OS),
    ("split", ["Bins / Libs", "Bins / Libs", "Bins / Libs"], C_BINS),
    ("split", ["App A", "App B", "App C"], C_APP),
]

# Docker stack (5 rows) — Infra, Host OS, Docker Engine, Bin/Libs x3, App x3
dk_rows = [
    ("full", "Infrastructure", C_INFRA, None),
    ("full", "Host Operating System", C_HOST, None),
    ("full", "Docker Engine", C_ENGINE, None),
    ("split", ["Bins / Libs", "Bins / Libs", "Bins / Libs"], C_BINS),
    ("split", ["App A", "App B", "App C"], C_APP),
]

max_rows = max(len(vm_rows), len(dk_rows))
stack_h = max_rows * ROW_H

total_w = MARGIN * 2 + STACK_W * 2 + STACK_GAP
total_h = MARGIN * 2 + TITLE_H + stack_h

vm_x0 = MARGIN
dk_x0 = MARGIN + STACK_W + STACK_GAP
stack_top_y = MARGIN + TITLE_H
stack_bottom_y = stack_top_y + stack_h  # baseline shared by both stacks


def render_stack(x0, rows):
    parts = []
    y = stack_bottom_y
    for kind, *rest in rows:
        y -= ROW_H
        if kind == "full":
            label, stroke, sub = rest
            parts.append(full_row(x0, y, label, stroke, sub))
        else:
            labels, stroke = rest
            parts.append(split_row(x0, y, labels, stroke))
    return "\n".join(parts)


svg_parts = []
svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{total_h}" '
                  f'viewBox="0 0 {total_w} {total_h}">')
svg_parts.append(f'  <rect x="0" y="0" width="{total_w}" height="{total_h}" fill="{BG}"/>')

svg_parts.append(stack_title(vm_x0, MARGIN + 34, "Virtual Machines"))
svg_parts.append(stack_title(dk_x0, MARGIN + 34, "Containers"))

svg_parts.append(render_stack(vm_x0, vm_rows))
svg_parts.append(render_stack(dk_x0, dk_rows))

svg_parts.append('</svg>')

svg = "\n".join(svg_parts)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diag_vm_vs_docker.svg")
with open(out_path, "w") as f:
    f.write(svg)
print("wrote", out_path, total_w, total_h)
