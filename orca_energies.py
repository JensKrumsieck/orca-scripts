import argparse
import csv
import glob
from itertools import dropwhile, takewhile
import os
import re
from babel.numbers import format_decimal

### ARGPARSE ###
parser = argparse.ArgumentParser(prog='orca_energies')
parser.add_argument(
    "folder", help="specify folder path to *_property.txt files")
args = parser.parse_args()
### END ARGPARSE ###

### VARIABLES ###
block_start = "$ THERMOCHEMISTRY_Energies"
block_end = "$# -------------------------------------------------------------"
regex = '^[A-Za-z\W]* (-?\d+[.,]?\d+)'
energies = []
format = "#.###########"
### END VARIABLES ###

# energies holder class


class EnergyInfo:
    def __init__(self, name, electronic, inner, enthalpy, gibbs):
        self.name = name
        self.electronic = electronic
        self.inner = inner
        self.enthalpy = enthalpy
        self.gibbs = gibbs

    def __repr__(self):
        return "\nEnergyInfo of {0}\n\telectronic:\t{1}\n\tinner:\t\t{2}\n\tenthalpy:\t{3}\n\tgibbs:\t\t{4}".format(
            self.name, self.electronic, self.inner, self.enthalpy, self.gibbs)


# read files in folder
search = glob.escape(args.folder)+"/*_property.txt"
files = glob.glob(search)
print(str(len(files)) + " property.txt-files found!")

# iterate files
for file in files:
    with open(file, 'r') as handle:
        electronic = 0
        enthalpy = 0
        gibbs = 0
        inner = 0
        dropped = dropwhile(lambda x: block_start not in x,
                            handle)  # drop all before block_start
        taken = takewhile(lambda x: block_end not in x,
                          dropped)  # drop all after block_end
        for line in taken:
            if "Electronic Energy" in line:
                electronic = re.match(regex, line)
            if "Inner Energy" in line:
                inner = re.match(regex, line)
            if "Enthalpy" in line:
                enthalpy = re.match(regex, line)
            if "Gibbs Energy" in line:
                gibbs = re.match(regex, line)
        try:
            energies.append(EnergyInfo(os.path.basename(file),
                        electronic[1], inner[1], enthalpy[1], gibbs[1]))
        except: print(f"{file} failed!")

# to csv
newfile = args.folder + "/energies.csv"
print("writing to " + newfile)
with open(newfile, "w", newline="") as csvfile:
    cw = csv.writer(csvfile, delimiter=";")
    cw.writerow(['Name', 'Electronic Energy',
                'Inner Energy', 'Enthalpy', 'Gibbs Energy'])
    for e in energies:
        cw.writerow([e.name,
                     format_decimal(e.electronic, locale='de', format=format),
                     format_decimal(e.inner, locale='de', format=format),
                     format_decimal(e.enthalpy, locale='de', format=format),
                     format_decimal(e.gibbs, locale='de', format=format)])

print("done 😎")
