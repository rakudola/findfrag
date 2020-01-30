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
sequence_infile = "C:/Users/spectrum/Downloads/recsvfiles/SA sequence.csv"
fragments_infile = "C:/Users/spectrum/Downloads/recsvfiles/csv for blast.csv"
outfile_name = "C:/Users/spectrum/Downloads/recsvfiles/SA sequence blast.csv"

"""
Editing code below this line will affect functionality!
"""

sequence_string = ""    # string to store entire sequence
fragments = {}          # dictionary to store the fragments
fragments_size = 0      # how many fragments there are (updated as file is read)
fragment_locations = {} # dictionary for start and end points of fragments

print("Reading files...")

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
    sequencefile = open(sequence_infile, 'r', newline = '')
    with sequencefile: # open sequence_infile
        sequence_reader = csv.reader(sequencefile) # create reader object; reads sequence_infile
        line_number = 0 # start at first line (0)
    
        for row in sequence_reader:
            sequence_string += row[0] # add each row to full sequence string
            line_number += 1          # 1 line read

except IOError: # If there is an error opening the sequence file, this will print
    print(sequence_infile + " could not be opened. Please ensure this file exists or is not in use by another program.")
except: # If there is an error reading the sequence file, this will print
    print("Error reading " + sequence_infile)


print("Finding fragments in sequence...")

for i in range(0, fragments_size):
    fragment_locations[fragments[i]] = [] # create new location list for fragment
    
    # find each fragment instance in sequence
    res = [j for j in range(len(sequence_string)) if sequence_string.startswith(fragments[i], j)]
    
    for j in range(len(res)):
        # create string with start and end position of fragment; add to dictionary
        fragment_locations[fragments[i]] += [str(START_POSITION + res[j]) + ", " + str(START_POSITION + res[j] + (len(fragments[i]) - 1))]

print("Writing to output file...")

try:
    outfile = open(outfile_name, 'w', newline = '')
    with outfile: # create/open output file
        writer = csv.writer(outfile, delimiter=',') # create writer object; writes fragment locations
        writer.writerow(["Fragment"] + ["# of Occurences"] + ["Start, End"]) # creates 2 headers
    
        for i in range(0, fragments_size):
            # populates rows with fragment title + # occurences + locations
            writer.writerow([fragments[i]] + [len(fragment_locations[fragments[i]])] + fragment_locations[fragments[i]])

except IOError: # If there is an error opening the outfile, this will print
    print(outfile_name + " could not be opened. Please ensure this file is not in use by another program.")
except: # If there is an error printing to the output file, this will print
    print("Error printing to " + outfile_name)
    


print("Complete! Output file: " + outfile_name)