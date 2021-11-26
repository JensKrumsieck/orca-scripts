#!/usr/bin/env python
import os
import sys
import shutil
import re

# Creates Shellscript for TU BS AC/OC Cluster
bin = os.path.dirname(os.path.realpath(__file__))
dir = os.getcwd()
file = sys.argv[1]
if len(sys.argv) > 2:
	mem = sys.argv[2]
else:
	mem = ''

print '#### Enqueueing ORCA 5.0 Script ####'
print 'Working Directory is ' + dir
print 'Filename is '+ file

src = bin + '/orca5_submit.sh'
dest = dir + '/' + file + '.sh'
print 'copying template script ' + src + ' to ' + dest
shutil.copy(src,dest)

handle = open(dir + '/' + file, 'r')
lines = handle.readlines()
for line in lines:
    if line.find('nprocs') != -1:
	find = line
m = re.search(r'[nprocs ]\d+', find)
procs=m.group(0).strip()
print procs + ' processors requested'
if(mem != ""):
	os.system('sbatch -n ' + procs + ' -p ' + procs + '-core' + '-' + mem + ' ' + dest)
else:
	os.system('sbatch -n ' + procs + ' -p ' + procs + '-core' + ' ' + dest)