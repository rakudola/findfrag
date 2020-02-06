# Code

[find fragment.py](https://github.com/rakudola/findfrag/blob/master/find%20fragment.py)
: Find given fragments in a single sequence

[find fragment_multiseq.py](https://github.com/rakudola/findfrag/blob/master/find%20fragment_multiseq.py)
: Find given fragments in multiple sequences

### Note on input/output files
**If you are using Spyder:** The filepaths for the in-/outfile variables can be created based on the directory the code is in
- e.g., "../SA sequence.csv"

**If you are using Canopy:** The full filepaths are needed for the in-/outfiles
- e.g., "C:/Users/Downloads/findfrag/Input/SA sequence.csv"
### To change input/output files
Change the following variables (v1.1.0)
```python
16 sequence_infile = "C:/Users/spectrum/Downloads/recsvfiles/SA sequence.csv"
17 fragments_infile = "C:/Users/spectrum/Downloads/recsvfiles/csv for blast.csv"
18 outfile_name = "C:/Users/spectrum/Downloads/recsvfiles/SA sequence blast.csv"
```

# Directory
[combine](https://github.com/rakudola/findfrag/tree/master/combine)
: Related project; base code to combine and analyze sequences for RA sick and healthy albumin written by Lavender

[old versions](https://github.com/rakudola/findfrag/tree/master/old%20versions)
: Old versions of the program and changelog

[package](https://github.com/rakudola/findfrag/tree/master/package)
: Contains the base single-sequence program + example input and output files

# find fragment.py
This program takes:
- input sequence (csv file)
- fragments to find in sequence (csv file)

and outputs:
- where and how many times the fragments were found in the input sequence (csv file)

## File formatting
### Input sequence file
Program will ONLY read first cell in each row. If you need to break up the sequence, please ensure the pieces of the sequence are all in the first cell of their own rows. Please do not include any extra data in the csv, including headers, as this may add the extra, unwanted data to the sequence.

### Input fragment file
Program will ONLY read first cell in each row. Please put one fragment in the first cell of each row.

### Output file
**Example data**

Fragment | # of Occurences | Start, End 
--- | --- | ---
abc | 1 | (1, 3) 
efg | 1 | (4, 6)

The third column gives the fragment's start and end position in the sequence.

If there are multiple occurences of the fragment, the locations will continue printing to the right in the fragment's row without column headers.

# find fragment_multiseq.py
This program takes:
- input sequences (csv or txt file; see File formatting: Input sequence file)
- fragments to find in sequences (csv file)

and outputs:
- where the fragments were found in the input sequences (csv file)

## File formatting
### Input sequence file
Program will take the protein ID from whatever is between ```>sp|``` and the next ```|```. The sequence will be read from the next line (or row) to the next line (or row) starting with ```>```.

**.txt Example**
```
>sp|Q6ZSK4|NTAS1_HUMAN Putative uncharacterized protein NTM-AS1 OS=Homo sapiens OX=9606 GN=NTM-AS1 PE=5 SV=1
MKGQEGIRGEGCTDPEIKASPQMWAARFRGMRSRFSPLFSQATEMGPRVSAGWCLSGGGR
KVSSLQGDFPPGGFWALSNDSALSLPPLSLPHPHPLRPPGLGVNEFTQGLHPPLHPAASV
FQTCFYRKPHYCSTLRPTTT
```

### Input fragment file
Program will ONLY read first cell in each row. Please put one fragment in the first cell of each row.

### Output file
**Example data**

Protein ID | Fragment 1 | Fragment 2
--- | --- | ---
ABC123 | (1, 3) | (2, 4) (6, 8) 
DEF456 | (5, 7) (10, 12) | (8, 10)

The fragment locations are formatted (start position, end position).

If the fragment is found multiple time in one protein sequence, the locations will all be in that fragment's column separated by a space.
