from collections import OrderedDict
from operator import itemgetter
import sys, os
import math
import csv
from io import StringIO

# returns a drug dictionary from file
def get_drugs_from_file(infilename,idx,length):
    print("processing chunk",idx+1,"of",length)
    drugs = {} # drug name, perscribers, total_cost
    # I picked cp437 encoding since there is one line which needs it in the big input file
    # code also runs with utf-8
    with open("./tmp_folder_for_files/"+infilename, encoding="cp437") as f:
        for line in f:
            # use the csv reader parser to handle " commas, in, quotes "
            linedata = csv.reader(StringIO(line)).__next__()
            if(linedata[0].isdigit()): # skip title lines
                cost = float(linedata[4])
                pid  = int(linedata[0])
                drug = linedata[3]
                if(drug in drugs):
                    drugs[drug]['perscribers'].add(pid)
                    drugs[drug]['total_cost'] += cost
                else:
                    drugs[drug] = {'drug':drug,'perscribers':{pid},'total_cost':cost}
    return drugs

# returns a drug dictionary that is the union of all the dictionaries in the list
def merge_drugs(list_of_drugs):
    new_drugs = {}
    for drugs in list_of_drugs:
        in_this_not_new = drugs.keys() - new_drugs.keys()
        in_both = new_drugs.keys() & drugs.keys()
        for key in in_this_not_new:
            new_drugs[key] = drugs[key]
        for drug in in_both:
            new_drugs[drug]['perscribers'].update(drugs[drug]['perscribers'])
            new_drugs[drug]['total_cost'] += drugs[drug]['total_cost']
    return(new_drugs)

# writes the output to top_cost_drug.txt sorted and formatted
def write_output(drugs):
    outf = open("./output/top_cost_drug.txt",'w', encoding="cp437")
    sdrugs = sorted(drugs.values(), key=lambda k: (k.get('total_cost'), k.get('drug')), reverse=True)
    outf.write("drug_name,num_prescriber,total_cost\n")
    for drug in sdrugs:
        price = "{0:.2f}".format(round(drug['total_cost'],2)).rstrip('0').rstrip('.')
        outf.write(str(drug['drug'])+","+str(len(drug['perscribers']))+","+price+"\n")
