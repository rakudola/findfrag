# Note on input/output files
**If you are using Spyder:** The filepaths for the in-/outfile variables can be created based on the directory the code is in
- e.g., "../SA sequence.csv"

**If you are using Canopy:** The full filepaths are needed for the in-/outfiles
- e.g., "C:/Users/Downloads/findfrag/Input/SA sequence.csv"
## To change input/output files
Change the following variables (v1.1.0)
```python
16 sequence_infile = "C:/Users/spectrum/Downloads/recsvfiles/SA sequence.csv"
17 fragments_infile = "C:/Users/spectrum/Downloads/recsvfiles/csv for blast.csv"
18 outfile_name = "C:/Users/spectrum/Downloads/recsvfiles/SA sequence blast.csv"
```

# Directory
[combine folder](https://github.com/rakudola/findfrag/tree/master/combine)
: Related project; base code to combine and analyze sequences for RA sick and healthy albumin written by Lavender

[package folder](https://github.com/rakudola/findfrag/tree/master/package)
: Contains the base program + input and output files of a run.

# What is this program?
This program takes:
- input sequence (csv file)
- fragments to find in sequence (csv file)

and outputs:
- where and how many times the fragments were found in the input sequence (csv file)

# File formatting (v1.1.0)
## Input sequence file
Program will ONLY read first cell in each row. If you need to break up the sequence, please ensure the pieces of the sequence are all in the first cell of their own rows. Please do not include any extra data in the csv, including headers, as this may add the extra, unwanted data to the sequence.

## Input fragment file
Program will ONLY read first cell in each row. Please put one fragment in the first cell of each row.

## Output file
**Example data**

Fragment | # of Occurences | Start, End 
--- | --- | ---
abc | 1 | (1, 3) 
efg | 1 | (4, 6)

The third column gives the fragment's start and end position in the sequence.

If there are multiple occurences of the fragment, the locations will continue printing to the right in the fragment's row without column headers.
