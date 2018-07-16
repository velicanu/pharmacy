from collections import OrderedDict
from operator import itemgetter
import os
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

# statinfo = os.stat("bigfile.txt")
chunksize = 2**25 # about 25MB
statinfo = os.stat("xaa")
size = statinfo.st_size
split = math.ceil(size/chunksize)
step = int(size/split)
print("total size = "+str(size))
print("splitting into",split,"groups")
begin = []
end = []
drugs = {} # drug name, perscribers, total_cost
# with open("bigfile.txt") as f:
if(False):
    with open("xaa") as f:
        for line in f:
            pass
if(True):
    # with open("xaa") as f:
    with open("xaa") as f:
        for i in range(split):
            # print(i)
            f.seek(step*i)
            f.readline()
            here = f.tell()
            if(i==0):
                begin.append(0)
            else:
                begin.append(here)
                end.append(here)
            f.seek(here)
            print("seek to "+str(here))
            print(f.readline())
        end.append(size)
        print(begin)
        print(end)

        if(True):
            for idx,loc in enumerate(begin):
                print(loc,"to",end[idx])
                f.seek(loc)
                data = f.read(end[idx]-loc)
                # for line in csv.reader(data):
                    # print(line)
                for line in data.splitlines():
                    linedata = csv.reader(StringIO(line)).__next__()
                    # linedata = line.split(',')
                    if(linedata[0].isdigit()): # skip title lines
                        addline(linedata, drugs)
                    # if "5,000" in line:
                        # print(line)
                        # print(linedata)
                        # print(drugs[linedata[3]])
                        # break

                # ['1891717344', 'JAMES', 'HELEN', 'PROCHLORPERAZINE MALEATE', '387.41']
# print(drugs)
print(type(drugs.get))
# print(drugs['ALPRAZOLAM'])
# print(type(drugs))
# s = [(k, drugs[k]) for k in sorted(drugs, key=drugs.get['total_cost'], reverse=True)]
# print(type(s))
sdrugs = sorted(drugs.values(), key=lambda k: k.get('total_cost'), reverse=True)
print(type(sdrugs))
outf = open('top_cost_drug.txt','w')
for drug in sdrugs:
    outf.write(str(drug['drug'])+","+str(len(drug['perscribers']))+","+"{0:.2f}".format(round(drug['total_cost'],2))+"\n")
    # break
# print(sdrugs[0])
# print(sdrugs[1])
# sdrugs = OrderedDict(sorted(drugs.items(), key = itemgetter('total_cost'), reverse = True))
# flag = True
# for k,v in sdrugs:
    # print(k,v)
    # if(flag):
        # flag = False
    # else:
        # break
