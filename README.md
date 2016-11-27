# rawfile_organizer
a simple Python script which organizes raw image files imported from a DSLR camera

# Purpose of this script
0. make a directory, rawfiles/
0. move all raw files to rawfiles/
0. remove all the raw files in rawfiles/ which do not have the corresponding jpeg files

# Implementation
For 1: 
* check if the directory exists, or create it

For 2:
* move all raw files

For 3:
* make a list of filenames of the raw files
* remove all entries which have the same file name of the jpeg files.
* delete the raw files left in the list from the disk


