from collections import OrderedDict
from operator import itemgetter
import sys, os
import math
import csv
from io import StringIO

def addline(linedata, drugdict):
    cost = float(linedata[4])
    pid  = int(linedata[0])
    drug = linedata[3]
    if(drug in drugdict.keys()):
        # add perscriber to list of perscribers of this drug if not already there, then add cost to total cost
        if(pid not in drugdict[drug]['perscribers'].keys()):
            drugdict[drug]['perscribers'][pid] = pid
        drugdict[drug]['total_cost'] += cost
    else:
        # add new drug to dictionary with first perscriber
        drugdict[drug] = {'drug':drug,'perscribers':{pid:pid},'total_cost':cost}

# ['1891717344', 'JAMES', 'HELEN', 'PROCHLORPERAZINE MALEATE', '387.41']

infilename = sys.argv[1]
outfilename = sys.argv[2]
outf = open(outfilename,'w')

chunksize = 2**25 # about 25MB
statinfo = os.stat(infilename)
size = statinfo.st_size
split = math.ceil(size/chunksize)
step = int(size/split)
# print("total size = "+str(size))
# print("splitting into",split,"groups")
begin = []
end = []
drugs = {} # drug name, perscribers, total_cost
# with open("bigfile.txt") as f:
if(True):
    with open(infilename) as f:
        for i in range(split):
            f.seek(step*i)
            # f.__next__()
            # f.readline()
            # print(f.readline())
            here = step*i+len(f.readline())
            there = here + len(f.readline())
            # print("seek to "+str(here))
            f.seek(here)
            f.readline()
            # print(f.readline())
            f.seek(here)
            # print(f.read(there-here))
            if(i==0):
                begin.append(0)
            else:
                begin.append(here)
                end.append(here)
            # print(f.readline())
            # print(f.readline())
            
        end.append(size)
        # print(begin)
        # print(end)
        ind = int(sys.argv[3])
        f.seek(begin[ind])
        stuff = f.read(end[ind]-begin[ind])
        outf.write(stuff)
        sys.exit(1)
        if(True):
            for idx,loc in enumerate(begin):
                print(loc,"to",end[idx])
                f.seek(loc)
                data = f.read(end[idx]-loc)
                print(data[-100:])
                for line in data.splitlines():
                    linedata = csv.reader(StringIO(line)).__next__()
                    if(linedata[0].isdigit()): # skip title lines
                        addline(linedata, drugs)

print(type(drugs.get))
sdrugs = sorted(drugs.values(), key=lambda k: k.get('total_cost'), reverse=True)
print(type(sdrugs))
outf.write("drug_name,num_prescriber,total_cost\n")
for drug in sdrugs:
    outf.write(str(drug['drug'])+","+str(len(drug['perscribers']))+","+"{0:.2f}".format(round(drug['total_cost'],2))+"\n")
