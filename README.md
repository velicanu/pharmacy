# Pharmacy Counting: coding challange solution for Insight Data Engineering.

Since it was not clear what the input files are going to look like, I've decided that everything (minus the README.md file) in the ```./input``` directory is meant to be processed. I've also assumed that those files will be in the general CSV format as shown in the two example files shown. I didn't code extra checks in my submission since in real world problems I've had to solve I would have selected valid CSV input in the step to generate the list of files to run on. 

Furthermore, I've decided to split the input files given into temporary chunks of 150M files. I do this because I'm used to running with multiple machines on multiple files, which would be needed for datasets exceeding 100GB or so. I know it is not efficient to duplicate data and could crash if the total size of files in a folder is bigger than half the available free space.

I'm also doing this to showcase that I know how to split the problem into parallelizable chunks, know the importance of preprocessing data, how to run in parallel then merge the output to get the final result. My code uses the python multiprocessing library to "parallel process" this data for showcasing purposes, for really big data sets I would use submission systems to multiple machines in hadoop. 

For the order of drugs I've assumed descending order also applies to drug name in case of a tie, so something like this:
```
ADRUG,5,1200
VDRUG,2,1000
CDRUG,3,1000
```
For the total cost of drugs I am dropping the last zero of the output in order to pass the first test and because that seems to be the format the data is provided in.

I would be happy to discuss my decisions or code further. 

## To manually run

```bash
./run.sh
```
Will run the program on all files in the ```./input/``` directory and put the ```top_cost_drug.txt``` file in the ```./output``` directory.
