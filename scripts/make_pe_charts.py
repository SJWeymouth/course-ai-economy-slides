#!/usr/bin/env python3
"""Public Event ('Who Controls AI?') concept diagrams.
Georgetown palette, matching scripts/make_day6_charts.py.
Two figures: the two meanings of 'control', and the closing variant
with every cell marked contested."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os, sys

NAVY="#041e42"; BLUE="#365f91"; PALE="#dce4ed"; MUTED="#71839b"
RED="#b23a48"; PAPER="#ffffff"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":18,
    "figure.facecolor":PAPER,"savefig.facecolor":PAPER})
OUT=sys.argv[1] if len(sys.argv)>1 else os.path.expanduser("~/course-ai-economy-slides/assets")
os.makedirs(OUT,exist_ok=True)

def box(ax,x,y,w,h,fc,ec=None,lw=1.5):
    ax.add_patch(FancyBboxPatch((x-w/2,y-h/2),w,h,
        boxstyle="round,pad=0.012,rounding_size=0.02",
        facecolor=fc,edgecolor=ec if ec else fc,linewidth=lw))

def save(fig,name):
    p=os.path.join(OUT,name); fig.savefig(p,dpi=150,bbox_inches="tight",pad_inches=0.25)
    plt.close(fig); print("wrote",p)

def two_meanings(contested=False):
    fig,ax=plt.subplots(figsize=(13,6.6)); ax.axis("off")
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    # Two columns
    for x,title,sub,q in [
        (0.26,"Control the technology","Does the AI do\nwhat we intend?","alignment · safety tests · oversight"),
        (0.74,"Control the stack","Who owns the chips, compute,\nmodels, and rules of access?","chips · data centers · models · access")]:
        box(ax,x,0.55,0.42,0.68,PALE if x<0.5 else "#e9eef4",ec=NAVY,lw=2)
        ax.text(x,0.79,title,ha="center",va="center",fontsize=22,fontweight="bold",color=NAVY)
        ax.text(x,0.60,sub,ha="center",va="center",fontsize=18,color=NAVY)
        ax.text(x,0.37,q,ha="center",va="center",fontsize=14,style="italic",color=MUTED)
    if contested:
        for x in (0.27,0.73):
            ax.text(x,0.245,"CONTESTED",ha="center",va="center",fontsize=17,
                    fontweight="bold",color=RED)
        ax.text(0.5,0.06,"Nobody fully holds either kind of control.",
                ha="center",va="center",fontsize=17,style="italic",color=RED)
    else:
        ax.text(0.5,0.06,"Same word, two different questions.",
                ha="center",va="center",fontsize=17,style="italic",color=MUTED)
    save(fig,"pe_control_contested.png" if contested else "pe_control_two_meanings.png")

two_meanings(False)
two_meanings(True)
