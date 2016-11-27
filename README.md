# Rawfile Organizer
This simple Python script organizes raw image files imported from a DSLR camera which saves both a compressed and a raw image files. (JPEG and CR2 format as default, respectively)

# Key operations of this script
0. relocate all raw files to a separted directory, named rawfiles/
0. remove all the raw files in rawfiles/ which do not have corresponding JPEG files

# Usage
* In a terminal,
```bash
$> python rawfile_organizer.py
```

# Implementation Details
For 1: 
* check if the directory exists, or create it

For 2:
* move all raw files

For 3:
* make a list of filenames of the raw files
* remove all entries which have the same file name of the jpeg files.
* delete the raw files left in the list from the disk

# License
Rawfile Organizer is released under the MIT license.
