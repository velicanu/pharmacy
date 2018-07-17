# Overview of code
## basic.py - provides the necessary functions to solve subparts of the problem.
### Overview of functions in basic.py
```python
def get_drugs_from_file
```
 - This efficiently reads the input text file and stores the information in a dictionary.

```python
def merge_drugs
```
 - This merges dictionaries created from running on different files so that drugs costs and unique perscribers are added.
 - This makes it possible to parallelize the problem by combining the output of different pieces correctly.

```python
def write_output
```
 - This sorts the drugs by total cost and writes the output to the top_cost_drug file, matching the formatting given in the sample output file. 
 
## root.py - provides the necessary functions to solve subparts of the problem.
This is the main class which gets the drugs from each input file in parallel and merges and writes the result using the functions in basic. 
