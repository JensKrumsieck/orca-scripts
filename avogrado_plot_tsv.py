import argparse
import os
from matplotlib import pyplot as plt
import pandas as pd
from util.settings import applySettings, colors, applyAxisSettings

applySettings()

### ARGPARSE ###
parser = argparse.ArgumentParser(prog='UV/Vis Plotter')
parser.add_argument("files", help="specify csv files", nargs='+')
parser.add_argument("-b", "--bars", help="bars")
parser.add_argument("-n", "--nonorm", action='store_true',  help="do not normalize")
parser.add_argument("-l", "--labels", nargs='+',  help="labels")
args = parser.parse_args()

### END ARGPARSE ###


def getMax(y: pd.Series):
    return y.max()


# Paths
paths = args.files
labels = args.labels
bars = args.bars
hasLabels = labels != None
normalize = not args.nonorm
df = pd.DataFrame()
for file in paths:
    filename, file_extension = os.path.splitext(file)
    if(file_extension == ".tsv"):
        df = pd.concat([df, (pd.read_csv(file, header=1, usecols=[0, 1], encoding='latin-1', sep="\t"))], axis=1)
    if(file_extension == ".csv"):
        df = pd.concat([df, (pd.read_csv(file, header=1, usecols=[0, 1], encoding='latin-1'))], axis=1)

num_spc = int(df.shape[1])
gmax = 0  # global max
fig, ax = plt.subplots()
for i in range(0, num_spc, 2):
    j = int(i/2)
    x = df.iloc[:, i]
    y = df.iloc[:, i+1]
    if normalize:
        # normalize
        max = getMax(y)
        y = y/max

    max = getMax(y)
    if(max > gmax):
        gmax = max
    if(not hasLabels or j >= len(labels)):
        plt.plot(x, y, colors[j])
    else:
        plt.plot(x, y, colors[j], label=labels[j])

if bars != None:
    bdf = pd.read_csv(bars, header=1, usecols=[0, 1], encoding="latin-1", sep="\t")
    x = bdf.iloc[:, 0]
    y = bdf.iloc[:, 1]
    plt.bar(x, y / y.max(), 3)
applyAxisSettings(ax, gmax, normalize)

plt.savefig("out/img.png", dpi=1200)
plt.savefig("out/img.svg", dpi=1200)
