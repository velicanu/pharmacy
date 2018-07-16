import os
import math
import csv

def addline(linedata, drugdict):
    print(linedata)
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
                    # print(line)
                    # csv.reader(line, skipinitialspace=True).__next__()
                    # csv.reader(line, quoting=csv.QUOTE_ALL, skipinitialspace=True).__next__()
                    # print( csv.reader(line, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True).__next__())
                        # print(linedata)
                    print(line.findall('"[^"]*"|[^,]+'))
                    break
                    linedata = line.split(',')
                    if(linedata[0].isdigit()): # skip title lines
                        addline(linedata, drugs)

                # ['1891717344', 'JAMES', 'HELEN', 'PROCHLORPERAZINE MALEATE', '387.41']
print(drugs)                
