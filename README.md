# rawfile_organizer
a simple Python script which organizes raw image files imported from a DSLR camera

# Purpose of this script
1. make a directory, rawfiles/
2. move all raw files to rawfiles/
3. remove all the raw files in rawfiles/ which do not have the corresponding jpeg files

# Implementation
For 1: 
a. check if the directory exists, or create it

For 2:
a. move all raw files

For 3:
a. make a list of filenames of the raw files
b. remove all entries which have the same file name of the jpeg files.
c. delete the raw files left in the list from the disk


