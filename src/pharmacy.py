from collections import OrderedDict
from operator import itemgetter
import sys, os
import math
import csv
from io import StringIO
import threading

def addline(linedata, drugdict):
    cost = float(linedata[4])
    pid  = int(linedata[0])
    drug = linedata[3]
    with drug_lock:
        if(drug in drugdict):
            # add perscriber to list of perscribers of this drug if not already there, then add cost to total cost
            if(pid not in drugdict[drug]['perscribers']):
                drugdict[drug]['perscribers'][pid] = pid
                drugdict[drug]['total_cost'] += cost
        else:
            # add new drug to dictionary with first perscriber
            drugdict[drug] = {'drug':drug,'perscribers':{pid:pid},'total_cost':cost}

def process_chunk(idx,loc,end,f):
    print("processing chunk",idx,"of",(len(end)-1))
    with file_lock:
        f.seek(loc)
        data = f.read(end[idx]-loc)
        for line in data.splitlines():
            linedata = csv.reader(StringIO(line)).__next__()
            if(linedata[0].isdigit()): # skip title lines
                addline(linedata, drugs)
                
# ['1891717344', 'JAMES', 'HELEN', 'PROCHLORPERAZINE MALEATE', '387.41']

drug_lock = threading.Lock()
file_lock = threading.Lock()

infilename = sys.argv[1]
outfilename = sys.argv[2]
outf = open(outfilename,'w', encoding="cp437")

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
mythreads = []
running_threads = []

# with open("bigfile.txt") as f:
with open(infilename, encoding="cp437") as f:

    for i in range(split):
        f.seek(step*i)
        here = step*i+len(f.readline())
        if(i==0):
            begin.append(0)
        else:
            begin.append(here)
            end.append(here)            
    end.append(size)

    for idx,loc in enumerate(begin):
        mythreads.append(threading.Thread(name=str("thread"+str(idx)), target=process_chunk, kwargs={'idx':idx,'loc':loc,'end':end,'f':f}))
    running_threads = mythreads.copy()
    while(mythreads):
        if(threading.active_count() < 5):
            runthread = mythreads.pop(0)
            runthread.start()
            running_threads.append(runthread)

    for thread in running_threads:
        thread.join()
        
sdrugs = sorted(drugs.values(), key=lambda k: k.get('total_cost'), reverse=True)
outf.write("drug_name,num_prescriber,total_cost\n")
for drug in sdrugs:
    price = "{0:.2f}".format(round(drug['total_cost'],2)).rstrip('0').rstrip('.')
    outf.write(str(drug['drug'])+","+str(len(drug['perscribers']))+","+price+"\n")
