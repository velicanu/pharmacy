import os
import math

def addline(linedata, drugdict):
    cost = int(linedata[4])
    pid  = int(linedata[0])

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
drugs = {}
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
                for line in data.splitlines():
                    linedata = line.split(',')
                    if(linedata[0].isdigit()): # skip title lines
                        addline(linedata)
                        print(linedata)
                    break

                # ['1891717344', 'JAMES', 'HELEN', 'PROCHLORPERAZINE MALEATE', '387.41']
                
