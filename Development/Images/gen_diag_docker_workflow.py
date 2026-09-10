#!/usr/bin/env python3
"""Docker workflow: two top-down swimlanes, top-aligned, single Image box,
with a horizontal 'docker push' crossing into the right lane.

Run from anywhere: `python3 gen_diag_docker_workflow.py`
Regenerates diag_docker_workflow.svg in this same Images/ folder.
"""

import os

BOX_W = 320
BOX_H = 90
ROW_GAP = 66
COL_GAP = 150
GROUP_PAD = 22
TITLE_IN = 54
MARGIN = 30

BG = "#282a36"
TXT = "#f8f8f2"
GROUP_FILL = "#33354499"
GROUP_STROKE = "#6272a4"
NODE_FILL = "#282a36"
LABEL_BG = "#44475a"

C_FILE = "#f8f8f2"
C_IMAGE = "#8be9fd"
C_RUN = "#50fa7b"
C_HUB = "#ff79c6"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def node(x, y, label, sub, stroke, fill=NODE_FILL, font=22):
    parts = [f'  <rect x="{x:.1f}" y="{y:.1f}" width="{BOX_W}" height="{BOX_H}" rx="10" '
             f'fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>']
    cx = x + BOX_W / 2
    if sub:
        parts.append(f'  <text x="{cx:.1f}" y="{y+BOX_H/2-10:.1f}" fill="{TXT}" font-size="{font}" '
                      f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle">{esc(label)}</text>')
        parts.append(f'  <text x="{cx:.1f}" y="{y+BOX_H/2+16:.1f}" fill="{TXT}" font-size="{font-6}" '
                      f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle" opacity="0.8">{esc(sub)}</text>')
    else:
        parts.append(f'  <text x="{cx:.1f}" y="{y+BOX_H/2+font*0.35:.1f}" fill="{TXT}" font-size="{font}" '
                      f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle">{esc(label)}</text>')
    return "\n".join(parts)


def v_arrow(x_center, y_top, y_bottom, label):
    parts = [f'  <line x1="{x_center:.1f}" y1="{y_top:.1f}" x2="{x_center:.1f}" y2="{y_bottom-10:.1f}" '
             f'stroke="{TXT}" stroke-width="2.5" marker-end="url(#arrow)"/>']
    mid_y = (y_top + y_bottom) / 2
    lw = 8 * len(label) + 20
    parts.append(f'  <rect x="{x_center-lw/2:.1f}" y="{mid_y-16:.1f}" width="{lw:.1f}" height="30" rx="5" fill="{LABEL_BG}"/>')
    parts.append(f'  <text x="{x_center:.1f}" y="{mid_y+6:.1f}" fill="{TXT}" font-size="18" '
                 f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle">{esc(label)}</text>')
    return "\n".join(parts)


def h_arrow(x_left, x_right, y_center, label):
    parts = [f'  <line x1="{x_left:.1f}" y1="{y_center:.1f}" x2="{x_right-10:.1f}" y2="{y_center:.1f}" '
             f'stroke="{TXT}" stroke-width="2.5" marker-end="url(#arrow)"/>']
    mid_x = (x_left + x_right) / 2
    lw = 8 * len(label) + 20
    parts.append(f'  <rect x="{mid_x-lw/2:.1f}" y="{y_center-16:.1f}" width="{lw:.1f}" height="30" rx="5" fill="{LABEL_BG}"/>')
    parts.append(f'  <text x="{mid_x:.1f}" y="{y_center+6:.1f}" fill="{TXT}" font-size="18" '
                 f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle">{esc(label)}</text>')
    return "\n".join(parts)


def group(x, y, w, h, title):
    parts = [f'  <rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="14" '
             f'fill="{GROUP_FILL}" stroke="{GROUP_STROKE}" stroke-width="2"/>']
    parts.append(f'  <text x="{x+w/2:.1f}" y="{y+36:.1f}" fill="{TXT}" font-size="26" font-weight="700" '
                 f'font-family="Helvetica, Arial, sans-serif" text-anchor="middle">{esc(title)}</text>')
    return "\n".join(parts)


# ---- geometry ----
group_w = BOX_W + 2 * GROUP_PAD
left_x = MARGIN
right_x = left_x + group_w + COL_GAP
group_y = MARGIN

content_top = group_y + TITLE_IN + GROUP_PAD
row1_y = content_top
row2_y = row1_y + BOX_H + ROW_GAP
row3_y = row2_y + BOX_H + ROW_GAP
row4_y = row3_y + BOX_H + ROW_GAP

left_box_x = left_x + GROUP_PAD
right_box_x = right_x + GROUP_PAD

left_group_h = (row3_y + BOX_H + GROUP_PAD) - group_y
right_group_h = (row4_y + BOX_H + GROUP_PAD) - group_y

total_w = right_x + group_w + MARGIN
total_h = group_y + max(left_group_h, right_group_h) + MARGIN

svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{total_w:.0f}" height="{total_h:.0f}" '
           f'viewBox="0 0 {total_w:.0f} {total_h:.0f}">')
svg.append(f'  <defs>\n'
           f'    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">\n'
           f'      <path d="M0,0 L0,6 L9,3 z" fill="{TXT}"/>\n'
           f'    </marker>\n'
           f'  </defs>')
svg.append(f'  <rect x="0" y="0" width="{total_w:.0f}" height="{total_h:.0f}" fill="{BG}"/>')

# group borders (top-aligned)
svg.append(group(left_x, group_y, group_w, left_group_h, "Local Workflow"))
svg.append(group(right_x, group_y, group_w, right_group_h, "Share via Docker Hub"))

# left column nodes
svg.append(node(left_box_x, row1_y, "Dockerfile", "(you write this)", C_FILE))
svg.append(node(left_box_x, row2_y, "Image", "(read-only snapshot)", C_IMAGE))
svg.append(node(left_box_x, row3_y, "Container", "(running instance)", C_RUN))

# right column nodes (row1 left empty for top alignment)
svg.append(node(right_box_x, row2_y, "Docker Hub", "(registry)", C_HUB))
svg.append(node(right_box_x, row3_y, "Teammate's machine", None, C_HUB))
svg.append(node(right_box_x, row4_y, "Container", "(same image, anywhere)", C_RUN))

# arrows within left column
col_cx = left_box_x + BOX_W / 2
svg.append(v_arrow(col_cx, row1_y + BOX_H, row2_y, "docker build"))
svg.append(v_arrow(col_cx, row2_y + BOX_H, row3_y, "docker run"))

# horizontal push arrow crossing into right column (row2 level)
svg.append(h_arrow(left_box_x + BOX_W, right_box_x, row2_y + BOX_H / 2, "docker push"))

# arrows within right column
col2_cx = right_box_x + BOX_W / 2
svg.append(v_arrow(col2_cx, row2_y + BOX_H, row3_y, "docker pull"))
svg.append(v_arrow(col2_cx, row3_y + BOX_H, row4_y, "docker run"))

svg.append('</svg>')

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diag_docker_workflow.svg")
with open(out_path, "w") as f:
    f.write("\n".join(svg))
print("wrote", out_path, total_w, total_h)
