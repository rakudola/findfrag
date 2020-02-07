# -*- coding: utf-8 -*-
import csv

"""
START_POSITION is the index of the first letter of the sequence.
e.g., if START_POSITION is 1, then a sequence is numbered like this:
    ABCDEFG
    1234567
if START_POSITION is 0, then a sequence is numbered like this:
    ABCDEFG
    0123456
"""
START_POSITION = 1

# If a file isn't opening, use its entire path here
fragments_infile = "test_frag1.csv"
sequence_infile = "test_input1.txt"
outfile_name = "test_output1.csv"

"""
Editing code below this line will affect functionality!
"""

fragments = {}          # dictionary to store the fragments
sequences = {}          # dictionary to store sequences
fragments_size = 0      # how many fragments there are (updated as file is read)
infile_type = ""

"""
Main code begins here
"""

print("Reading files...")

if (sequence_infile.find(".csv") != -1):
    infile_type = "csv"
elif (sequence_infile.find(".txt") != -1):
    infile_type = "txt"
else:
    print("Input filetype not supported. Please convert to .csv or .txt")

try: # try to open and read fragment file
    fragmentsfile = open(fragments_infile, 'r', newline = '')
    with fragmentsfile: # open fragments_infile
        fragments_reader = csv.reader(fragmentsfile) # create reader object; reads fragments_infile
        line_number = 0 # start at first line (0)
    
        for row in fragments_reader:
            fragments[line_number] = row[0]     # access fragment as string from csv row
            fragments_size += 1                 # 1 fragment added
            line_number += 1                    # 1 line read

except IOError: # If there is an error opening the fragment file, this will print
    print(fragments_infile + " could not be opened. Please ensure this file exists or is not in use by another program.")
except: # If there is an error reading the fragment file, this will print
    print("Error reading " + fragments_infile)
    
try:
    protein_seq = ""
    protein_id = ""

    if (infile_type == "csv"):
        """Not fixed, please fix :("""
        sequencefile = open(sequence_infile, 'r', newline = '')
        with sequencefile: # open sequence_infile
            sequence_reader = csv.reader(sequencefile) # create reader object; reads sequence_infile
            first_row = True # True if reader is on first row
        
            for row in sequence_reader:
                if (row[0][0] == '>' ):
                    if (not first_row):
                        sequences[protein_id] = protein_seq
                        protein_id = ""
                        protein_seq = ""
                        
                    id_loc = row[0].find('|') + 1 # find location of first |, ID starts next character

                    while (row[0][id_loc] != "|" and row[0][id_loc] != "\n"):
                        protein_id += row[0][id_loc]
                        id_loc += 1

                else:
                    protein_seq += row[0]
                
                first_row = False
            
            sequences[protein_id] = protein_seq
            protein_id = ""
            protein_seq = ""

    elif(infile_type == "txt"):
        with open(sequence_infile, 'r', newline = '\n') as sequencefile:
            line = sequencefile.readline()
            while line: # for every line

                if (line[0] == '>'):
                    id_loc = line.find('|') + 1 # find location of first |, ID starts next character

                    while (line[id_loc] != "|" and line[id_loc] != "\n"):
                        protein_id += line[id_loc]
                        id_loc += 1

                else:
                    protein_seq += line

                try:
                    line = sequencefile.readline()
                    if (line[0] == '>'):
                        sequences[protein_id] = protein_seq
                        protein_id = ""
                        protein_seq = ""
                except:
                    sequences[protein_id] = protein_seq
                    break

except IOError: # If there is an error opening the sequence file, this will print
    print(sequence_infile + " could not be opened. Please ensure this file exists or is not in use by another program.")
except: # If there is an error reading the sequence file, this will print
    print("Error reading " + sequence_infile)

print("Finding fragments in sequence & writing to output file...")

try:
    fragment_locations = {} # dictionary for start and end points of fragments

    with open(outfile_name, 'w', newline = '') as outfile:
        writer = csv.writer(outfile, delimiter = ',') # create writer object; writes fragment locations

        header_row = ["Protein ID"] # start header row with Protein ID
        for j in fragments:
            header_row += [fragments[j]] # fill in header row with the fragments

        writer.writerow(header_row)

    for i in sequences:
        for j in fragments:
            fragment_locations[j] = [] # create new location list for fragment
        
            # find each fragment instance in sequence
            res = [k for k in range(len(sequences[i])) if sequences[i].startswith(fragments[j], k)]
            
            for k in range(len(res)):
                # create string with start and end position of fragment; add to dictionary
                frag_start = str(START_POSITION + res[k])
                frag_end = str(START_POSITION + res[k] + (len(fragments[j]) - 1))
                fragment_locations[j] += ["(" + frag_start + ", " + frag_end + ")"]

        with open(outfile_name, 'a', newline = '') as outfile:
            writer = csv.writer(outfile, delimiter = ',') # create writer object; writes fragment locations
            new_row = [i]
            for j in fragment_locations:
                frag_locs = ""
                for k in fragment_locations[j]:
                    frag_locs += k + " "
                new_row += [frag_locs]
            writer.writerow(new_row)

except IOError: # If there is an error opening the outfile, this will print
    print(outfile_name + " could not be opened. Please ensure this file is not in use by another program.")
except: # If there is an error printing to the output file, this will print
    print("Error printing to " + outfile_name)

print("Complete! Output file: " + outfile_name)
