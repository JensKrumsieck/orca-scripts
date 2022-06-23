import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


def cm_to_inch(value):
    return value/2.54


def applySettings():
    plt.style.use(['science', 'nature', 'no-latex'])
    plt.rcParams["figure.figsize"] = (cm_to_inch(16), cm_to_inch(13))
    plt.rcParams["figure.dpi"] = 1200
    plt.rcParams["axes.labelsize"] = 11
    plt.rcParams["axes.titlesize"] = 9
    plt.rcParams["xtick.labelsize"] = 9
    plt.rcParams["ytick.labelsize"] = 9
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams["font.family"] = "Arial"


def colorMap(num_spc):
    colors = [(0, 0, 0), (1, 0, 0)]  # first color is black, last is red
    cm = LinearSegmentedColormap.from_list(
        "Custom", colors, N=20)
    cols = cm(np.linspace(0, 1, int(num_spc/2)))
    return cols


colors = ["#000000",  "#EF0000", "#336699",  "#3BC371", "#FEC211",  "#666699", "#FF6666",   "#CC6600", "#6699CC", "#99867A", "#999999", "#6B67BC", "#009999"]

from matplotlib.ticker import AutoMinorLocator
import pandas as pd


def forward(x):
    return 1e4/x


def inverse(x):
    return 1e4/x


def applyAxisSettings(ax, gmax, normalize):
    ax.legend()
    ax.tick_params(direction="out", top=False, right=False)
    ax.tick_params(which="minor", axis="y", right=False, direction="out")
    ax.tick_params(which="minor", axis="x", top=False, direction="out")
    secax = ax.secondary_xaxis('top', functions=(forward, inverse))
    secax.xaxis.set_minor_locator(AutoMinorLocator(2))
    secax.set_xlabel("$\mathregular{\\nu}$ /$\mathregular{10^3}$$\mathregular{cm^{-1}}$")
    ax.set_xlim(250, 1100)
    ax.set_ylim(0, gmax + 0.1*gmax)
    ax.set_xlabel("$\mathregular{\lambda}$ /nm")
    if normalize:
        ax.set_ylabel("norm. Abs.")
    else:
        ax.set_ylabel("rel. Abs.")