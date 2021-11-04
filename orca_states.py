import sys
import re
import argparse
import csv
from itertools import dropwhile, takewhile
from babel.numbers import format_decimal

### ARGPARSE ###
parser = argparse.ArgumentParser(prog='orca_uv')
parser.add_argument("filename", help="specify path to .out file")
parser.add_argument("-t", "--threshold", type=float,
                    default=0, help="specify path to .out file")

args = parser.parse_args()
### END ARGPARSE ###

### VARIABLES ###
block_start = "TD-DFT EXCITED STATES"
block_end = "TD-DFT-EXCITATION SPECTRA"
states = list()
blocks = list()
regex_transitions = "(\d*[a,b]) -> (\d*[a,b])[ ,:.]*(\d*[,.]?\d*)"
regex_state = "^STATE *(\d+)"
regex_block = "(^STATE *\d+.*)\n( *\d*[a,b] -> \d*[a,b][ ,:.]*\d*[,.]?\d* *\n)+"
### END VARIABLES ###

### PARSING ###


def parse_lines(lines: str):
    index = re.match(regex_state, lines).group(1)
    transitions = re.findall(regex_transitions, lines)
    return(index, transitions)

try:
    with open(args.filename, 'r') as file:
        dropped = dropwhile(lambda x: block_start not in x,
                            file)  # drop all before block_start
        taken = takewhile(lambda x: block_end not in x,
                          dropped)  # drop all after block_end
        # build blocks
        current = ""
        for line in taken:     
            current += line
        blocks = re.finditer(regex_block, current, re.MULTILINE)
        for no, block in enumerate(blocks):      
            states.append(parse_lines(block.group()))
except IOError:
    print("file not found at " + args.filename)
    sys.exit(1)  # exit with failure
### END PARSING ###

### PROCESSING ###
with open(args.filename + "_states.csv", "w", newline="") as csvfile:
    cw = csv.writer(csvfile, delimiter=";")
    for state in states:
        cw.writerow(['STATE', 'FROM', 'TO', "%"])  # header row
        sum = 0
        for trans in state[1]:  # transitions
            sum += float(trans[2])
        for trans in state[1]:  # transitions
            percentage = (float(trans[2])/sum)
            if percentage > args.threshold:
                cw.writerow([state[0], trans[0], trans[1],
                            format_decimal(percentage, locale="de")])
        cw.writerow([' ', ' ', ' ', " "])  # header row
### END PROCESSING ###
