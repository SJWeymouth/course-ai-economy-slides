#!/usr/bin/env python3
"""Day 6 concept diagrams for 'Institutional Risk and Alignment'.
Georgetown palette. Two figures: the intelligence-curse equilibrium break,
and the Anthropic pledge change (before/after)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

NAVY="#041e42"; BLUE="#365f91"; TAUPE="#8a7f75"; PALE="#dce4ed"; MUTED="#71839b"
RED="#b23a48"; PAPER="#ffffff"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":18,
    "figure.facecolor":PAPER,"savefig.facecolor":PAPER})
OUT=os.path.expanduser("~/course-ai-economy-slides/assets"); os.makedirs(OUT,exist_ok=True)

def box(ax, x, y, w, h, text, fc, tc, fs=15, ec=None, lw=1.5, style="round"):
    p=FancyBboxPatch((x-w/2, y-h/2), w, h,
        boxstyle=f"round,pad=0.012,rounding_size=0.02",
        facecolor=fc, edgecolor=ec if ec else fc, linewidth=lw)
    ax.add_patch(p)
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc, wrap=True)

def arrow(ax, x1, y1, x2, y2, color=NAVY, ls="-", lw=2.4):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2), arrowstyle="-|>",
        mutation_scale=22, lw=lw, color=color, linestyle=ls,
        shrinkA=2, shrinkB=2))

def save(fig,name):
    p=os.path.join(OUT,name); fig.savefig(p,dpi=150,bbox_inches="tight",pad_inches=0.2)
    plt.close(fig); print("wrote",p)

# ---------------------------------------------------------------------------
# 1. The intelligence curse: how advanced AI breaks the deal
# ---------------------------------------------------------------------------
fig,ax=plt.subplots(figsize=(12,6.8)); ax.axis("off")
ax.set_xlim(0,1); ax.set_ylim(0,1)
xc=[0.34,0.60,0.86]; w=0.235; h=0.20
# Row labels
ax.text(0.045,0.74,"Today",ha="left",va="center",fontsize=19,fontweight="bold",color=NAVY)
ax.text(0.045,0.26,"With\nadvanced\nAI",ha="left",va="center",fontsize=17,fontweight="bold",color=RED)
# Top row (today)
box(ax,xc[0],0.74,w,h,"People do the work\nand pay taxes",PALE,NAVY)
box(ax,xc[1],0.74,w,h,"Leaders gain\nmoney and power",BLUE,"#ffffff")
box(ax,xc[2],0.74,w,h,"Leaders invest\nin people",NAVY,"#ffffff")
arrow(ax,xc[0]+w/2,0.74,xc[1]-w/2,0.74)
arrow(ax,xc[1]+w/2,0.74,xc[2]-w/2,0.74)
# Bottom row (with AI)
box(ax,xc[0],0.26,w,h,"AI does\nthe work",PALE,NAVY)
box(ax,xc[1],0.26,w,h,"Leaders gain\nmoney and power",BLUE,"#ffffff")
box(ax,xc[2],0.26,w,h,"Less reason to\ninvest in people",PAPER,RED,ec=RED,lw=2.5)
arrow(ax,xc[0]+w/2,0.26,xc[1]-w/2,0.26)
arrow(ax,xc[1]+w/2,0.26,xc[2]-w/2,0.26,color=RED,ls=(0,(4,3)))
# divider line
ax.plot([0.03,0.99],[0.5,0.5],color="#d8dde3",lw=1.2)
save(fig,"day6_intelligence_curse.png")

# ---------------------------------------------------------------------------
# 2. Anthropic's pledge: unconditional -> conditional
# ---------------------------------------------------------------------------
fig,ax=plt.subplots(figsize=(12,6.2)); ax.axis("off")
ax.set_xlim(0,1); ax.set_ylim(0,1)
# left box: 2023
box(ax,0.25,0.56,0.40,0.44,"",NAVY,"#ffffff")
ax.text(0.25,0.72,"2023 pledge",ha="center",va="center",fontsize=20,fontweight="bold",color="#ffffff")
ax.text(0.25,0.56,"Pause training until we\ncan show it is safe",ha="center",va="center",fontsize=17,color="#ffffff")
ax.text(0.25,0.42,"Unconditional",ha="center",va="center",fontsize=15,style="italic",color=PALE)
# right box: 2026
box(ax,0.75,0.56,0.40,0.44,"",BLUE,"#ffffff")
ax.text(0.75,0.72,"2026 · RSP v3.0",ha="center",va="center",fontsize=20,fontweight="bold",color="#ffffff")
ax.text(0.75,0.56,"Slow down only if we lead\nthe race AND the risk is large",ha="center",va="center",fontsize=17,color="#ffffff")
ax.text(0.75,0.40,"Conditional",ha="center",va="center",fontsize=15,style="italic",color="#e5ebf3")
# arrow between
ax.add_patch(FancyArrowPatch((0.455,0.56),(0.545,0.56),arrowstyle="-|>",
    mutation_scale=30,lw=3,color=RED))
ax.text(0.50,0.66,"Feb 2026",ha="center",va="bottom",fontsize=15,fontweight="bold",color=RED)
# caption
ax.text(0.5,0.12,"The firm “pause until safe” promise became a conditional one.",
    ha="center",va="center",fontsize=16,color=MUTED,style="italic")
ax.set_ylim(0.02,1)
save(fig,"day6_pledge_change.png")

# ---------------------------------------------------------------------------
# 3. Resource curse vs intelligence curse (two icon cards)
# ---------------------------------------------------------------------------
from matplotlib.patches import Circle, Polygon, Rectangle
def oil_drop(ax, cx, cy, r, color):
    ax.add_patch(Circle((cx, cy), r, facecolor=color, edgecolor="none"))
    ax.add_patch(Polygon([(cx-r*0.92, cy+r*0.28),(cx+r*0.92, cy+r*0.28),(cx, cy+r*1.9)],
                 facecolor=color, edgecolor="none"))
def chip(ax, cx, cy, s, color):
    ax.add_patch(FancyBboxPatch((cx-s/2, cy-s/2), s, s,
        boxstyle="round,pad=0.002,rounding_size=0.01", facecolor=color, edgecolor="none"))
    for f in (-1,1):
        for t in (-0.28,0,0.28):
            ax.plot([cx+f*s/2, cx+f*(s/2+s*0.22)],[cy+t*s, cy+t*s],color=color,lw=3)
            ax.plot([cx+t*s, cx+t*s],[cy+f*s/2, cy+f*(s/2+s*0.22)],color=color,lw=3)
    ax.text(cx,cy,"AI",ha="center",va="center",fontsize=17,fontweight="bold",color="#ffffff")

fig,ax=plt.subplots(figsize=(12,6.0)); ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,1)
for cx,fc in [(0.27,PALE),(0.73,PALE)]:
    ax.add_patch(FancyBboxPatch((cx-0.20,0.24),0.40,0.60,
        boxstyle="round,pad=0.01,rounding_size=0.03",facecolor=fc,edgecolor="#c9cfd6",lw=1.5))
oil_drop(ax,0.27,0.66,0.052,NAVY)
chip(ax,0.73,0.66,0.10,BLUE)
ax.text(0.27,0.45,"Resource curse",ha="center",fontsize=20,fontweight="bold",color=NAVY)
ax.text(0.27,0.36,"Money comes from oil,\nnot from people",ha="center",va="top",fontsize=15,color="#333b45")
ax.text(0.73,0.45,"Intelligence curse",ha="center",fontsize=20,fontweight="bold",color=NAVY)
ax.text(0.73,0.36,"Money comes from AI,\nnot from people",ha="center",va="top",fontsize=15,color="#333b45")
ax.text(0.5,0.13,"Either way, leaders need people less.",ha="center",fontsize=17,color=MUTED,style="italic")
save(fig,"day6_two_curses.png")

# ---------------------------------------------------------------------------
# 4. Three mechanisms (icon panels)
# ---------------------------------------------------------------------------
import math
fig,ax=plt.subplots(figsize=(13,5.2)); ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,1)
cxs=[0.18,0.5,0.82]; icy=0.62
# Concentration: arrows converging to a dot
ax.add_patch(Circle((cxs[0],icy),0.028,facecolor=NAVY,edgecolor="none",zorder=5))
for a in range(0,360,60):
    dx,dy=math.cos(math.radians(a)),math.sin(math.radians(a))
    ax.add_patch(FancyArrowPatch((cxs[0]+0.11*dx,icy+0.11*dy),(cxs[0]+0.045*dx,icy+0.045*dy),
        arrowstyle="-|>",mutation_scale=14,lw=2,color=BLUE))
# Detachment: two boxes with a broken link
for f in (-1,1):
    ax.add_patch(FancyBboxPatch((cxs[1]+f*0.10-0.03,icy-0.03),0.06,0.06,
        boxstyle="round,pad=0.002,rounding_size=0.01",facecolor=BLUE,edgecolor="none"))
ax.plot([cxs[1]-0.05,cxs[1]+0.05],[icy,icy],color=MUTED,lw=2.5,ls=(0,(3,3)))
ax.plot([cxs[1]-0.018,cxs[1]+0.018],[icy+0.02,icy-0.02],color=RED,lw=3)
ax.plot([cxs[1]-0.018,cxs[1]+0.018],[icy-0.02,icy+0.02],color=RED,lw=3)
# Legitimacy: downward trend arrow
ax.add_patch(FancyArrowPatch((cxs[2]-0.09,icy+0.075),(cxs[2]+0.09,icy-0.075),
    arrowstyle="-|>",mutation_scale=22,lw=3.2,color=RED,
    connectionstyle="arc3,rad=0.25"))
# labels
labs=[("Concentration","gains go to a few"),("Detachment","leaders on autopilot"),
      ("Legitimacy","public trust falls")]
for cx,(t,s) in zip(cxs,labs):
    ax.text(cx,0.34,t,ha="center",fontsize=21,fontweight="bold",color=NAVY)
    ax.text(cx,0.25,s,ha="center",fontsize=15,color="#333b45")
save(fig,"day6_curse_mechanisms.png")

# ---------------------------------------------------------------------------
# 5. Outcomes: money circulates among the powerful, people left outside
# ---------------------------------------------------------------------------
fig,ax=plt.subplots(figsize=(12,6.6)); ax.axis("off"); ax.set_xlim(0,1); ax.set_ylim(0,1)
# top region: the AI economy among elites
ax.add_patch(FancyBboxPatch((0.16,0.52),0.68,0.36,
    boxstyle="round,pad=0.01,rounding_size=0.03",facecolor="#f2f5f9",edgecolor="#c9cfd6",lw=1.5))
ax.text(0.5,0.845,"The money stays among the powerful",ha="center",fontsize=17,
    fontweight="bold",color=NAVY)
nodes=[(0.30,0.66,"States\n(taxes)"),(0.5,0.66,"AI labs\n(rents)"),(0.70,0.66,"Big firms")]
for x,y,t in nodes:
    ax.add_patch(FancyBboxPatch((x-0.085,y-0.055),0.17,0.11,
        boxstyle="round,pad=0.006,rounding_size=0.02",facecolor=BLUE,edgecolor="none"))
    ax.text(x,y,t,ha="center",va="center",fontsize=14,color="#ffffff")
for x1,x2 in [(0.30,0.5),(0.5,0.70)]:
    ax.add_patch(FancyArrowPatch((x1+0.085,y+0.02),(x2-0.085,y+0.02),
        arrowstyle="-|>",mutation_scale=16,lw=2,color=NAVY,connectionstyle="arc3,rad=-0.3"))
    ax.add_patch(FancyArrowPatch((x2-0.085,y-0.02),(x1+0.085,y-0.02),
        arrowstyle="-|>",mutation_scale=16,lw=2,color=NAVY,connectionstyle="arc3,rad=-0.3"))
# broken arrow down to people
ax.add_patch(FancyArrowPatch((0.5,0.52),(0.5,0.28),arrowstyle="-|>",
    mutation_scale=20,lw=2.6,color=MUTED,linestyle=(0,(4,3))))
ax.plot([0.47,0.53],[0.42,0.38],color=RED,lw=4); ax.plot([0.47,0.53],[0.38,0.42],color=RED,lw=4)
# people box
ax.add_patch(FancyBboxPatch((0.36,0.13),0.28,0.12,
    boxstyle="round,pad=0.008,rounding_size=0.02",facecolor=PAPER,edgecolor=RED,lw=2.5))
ax.text(0.5,0.19,"Most people",ha="center",va="center",fontsize=16,fontweight="bold",color=RED)
ax.text(0.5,0.04,"There is little economic reason left to invest in ordinary people.",
    ha="center",fontsize=15,color=MUTED,style="italic")
save(fig,"day6_outcomes.png")
print("done")
