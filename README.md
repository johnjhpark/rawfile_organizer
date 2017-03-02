# Rawfile Organizer
This simple Python script help you organize raw image files imported from a DSLR camera which saves both compressed and raw image files. (JPEG and CR2 format as default, respectively. However, you can simply change the formats by modifying only one line of code)

# Key operations of this script
0. relocate all raw files to a separted directory, named /rawfiles
0. remove all the raw files in /rawfiles which do not have corresponding JPEG files in the working directory

# How to run
* In a terminal,
```bash
$> python rawfile_organizer.py
```

# Recommendation for the use of this script
0. copy this script file to the working directory where you import all JPEG and raw image files from your DSLR
0. Run this script as an initialization
0. Do your work: e.g.) look across the JPEG files and delete some of them that you don't want to keep any longer
0. Run this script again after you finish working on the files


# Implementation Details
Step 1: 
* check if the directory exists, or create it

Step 2:
* move all raw files

Step 3:
* make a list of filenames of the raw files
* remove all entries which have the same file name of the jpeg files.
* delete the raw files left in the list from the disk

# License
Rawfile Organizer is released under the MIT license.
