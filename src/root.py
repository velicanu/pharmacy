from basic import *
from os import listdir
from os.path import isfile, join
import multiprocessing as mp

# get all the input files
list_of_input_files = [f for f in listdir("./tmp_folder_for_files/") if isfile(join("./tmp_folder_for_files/", f))]
list_of_drugs = []

# set up parallel processing
cores = mp.cpu_count()
pool = mp.Pool(cores)
jobs = []

# make a list of drugs from each file, in parallel!
for idx,filename in enumerate(list_of_input_files):
    jobs.append( pool.apply_async(get_drugs_from_file,(filename,idx,len(list_of_input_files))))

# wait for the jobs to finish and append their work to a list
for job in jobs:
    list_of_drugs.append(job.get())
pool.close()

# merge the list of drugs from each file into one big list
print("merging dictionaries...")
merged_drugs = merge_drugs(list_of_drugs)

# write the output sorted by total drug cost
print("writing output...")
write_output(merged_drugs)

