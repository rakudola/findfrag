# Changelog

# find fragment.py

## v1.0.0
(2020/1/28)
- Base program

### v1.1.0
(2020/1/30)
- Minor code adjustments so program works in Canopy
- Cleaned up the try/except statements so that a message explaining the problem pops up instead of a Python-generated error message

# find fragment_multiseq.py

## v1.0.0
(2020/2/5)
- Base program

## v1.1.0
(2020/2/7)
- Output:

**Example data**

Protein ID | Fragment 1 | Fragment 2
--- | --- | ---
ABC123 | (1, 3) | (2, 4) (6, 8) 
DEF456 | (5, 7) (10, 12) | (8, 10)

The fragment locations are formatted (start position, end position).

If the fragment is found multiple time in one protein sequence, the locations will all be in that fragment's column separated by a space.

## v1.2.0
(2020/2/7)
- Output formatting changed

Output:

**Example data**

Peptide | Protein ID | (Start, End)
--- | --- | ---
ABCDEFG | ABC123 | (1, 7)
HIJKLMN | ABC123 | (8, 14)

Only fragments found in a sequence will be printed. If a fragment is found multiple times in a sequence, the (start, end) positions will continue printing in the row in cells to the right.
