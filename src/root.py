from basic import *
from os import listdir
from os.path import isfile, join
import multiprocessing as mp

# get all the input files
list_of_input_files = [f for f in listdir("./tmp_folder_for_files/") if isfile(join("./tmp_folder_for_files/", f))]
list_of_drugs = []

# make a list of drugs from each file
cores = mp.cpu_count()
pool = mp.Pool(cores)
jobs = []

for idx,filename in enumerate(list_of_input_files):
    jobs.append( pool.apply_async(get_drugs_from_file,(filename,idx,len(list_of_input_files))))
    # list_of_drugs.append(get_drugs_from_file(filename))

for job in jobs:
    list_of_drugs.append(job.get())

pool.close()

# merge the list of drugs from each file into one big list
print("merging dictionaries...")
merged_drugs = merge_drugs(list_of_drugs)

# write the output sorted by total drug cost
print("writing output...")
write_output(merged_drugs)

print("Done.")
