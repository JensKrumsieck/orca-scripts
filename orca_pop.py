import sys
import re
import argparse
import csv
from itertools import dropwhile, takewhile

### ARGPARSE ###
parser = argparse.ArgumentParser(prog='orca_pop')
parser.add_argument("filename", help="specify path to .out file")
parser.add_argument("-p", "--population", default="mulliken", type=str)
parser.add_argument("-m", "--metal", default="", type=str)

args = parser.parse_args()
### END ARGPARSE ###

### VARIABLES ###
block_start_loewdin = "LOEWDIN ATOMIC CHARGES AND SPIN POPULATIONS"
block_start_mulliken = "MULLIKEN ATOMIC CHARGES AND SPIN POPULATIONS"
block_end_loewdin = "LOEWDIN REDUCED ORBITAL CHARGES AND SPIN POPULATIONS"
block_end_mulliken = "MULLIKEN REDUCED ORBITAL CHARGES AND SPIN POPULATIONS"
block_start = block_start_mulliken if args.population == "mulliken" else block_start_loewdin
block_end = block_end_mulliken if args.population == "mulliken" else block_end_loewdin
pops = list()
block = ""
### END VARIABLES ###

### PARSING ###
try:
    with open(args.filename, 'r') as file:
        dropped = dropwhile(lambda x: block_start not in x,
                            file)  # drop all before block_start
        taken = takewhile(lambda x: block_end not in x,
                          dropped)  # drop all after block_end
        for line in taken:
            block += line
        rgx = "(\d+) *(\w{1,2}) *: *(-{0,1}\d.\d*) *(-{0,1}\d.\d*)"
        pops = re.findall(rgx, block)

except IOError:
    print("file not found at " + args.filename)
    sys.exit(1)  # exit with failure
### END PARSING ###

pop_sum = 0
pop_ligsum = 0
chrg_sum = 0
chrg_ligsum = 0
pop_m = 0
chrg_m = 0
delim = "\t"
with open(args.filename + "_pop_" + str(args.population) + ".txt", "w") as file:
    file.write("#" + delim + "Sym"+delim +
               "Charge"+delim + "Pop\n")
    for pop in pops:
        if args.metal != "":
            if(pop[1] != args.metal):
                pop_ligsum += float(pop[3])
                chrg_ligsum += float(pop[2])
            else:
                pop_m = float(pop[3])
                chrg_m = float(pop[2])
        pop_sum += float(pop[3])
        chrg_sum += float(pop[2])
        file.write(pop[0] + delim + pop[1] + delim + pop[2] + delim + pop[3] + "\n")
    
    file.write("Sum of charges: " + str(round(chrg_sum,4)) + "\n")
    file.write("Sum of populations: " + str(round(pop_sum,4)) + "\n")
    if args.metal != "":
        file.write("Sum of Non-Metal-Charges: " + str(round(chrg_ligsum,4)) + "\n")
        file.write("Sum of Non-Metal-Populations: " + str(round(pop_ligsum,4))+ "\n")
        file.write("Metal-Charge: " + str(round(chrg_m,4)) + "\n")
        file.write("Metal-Population: " + str(round(pop_m,4)) + "\n")
