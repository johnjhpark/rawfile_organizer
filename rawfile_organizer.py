"""
filename: rawfile_organizer.py
description: to keep the necessary raw image files in a separated location
created by John (johnjhparkprof@gmail.com) on Nov. 26 2016

usage:
    $cp rawfile_organizer.py /path/to/images/imported/from/your/dslr
    $python python rawfile_organizer.py
"""

# NOTICE: imported the top objects only for training purpose
import os
import shutil
import errno
# from os import makedirs, remove

# Step 1: check the directory exists, or create it
# TODO: support cross-platform (esp. Windows)


# Warning: current folder name format should be 'date_title'
split_character = '_'
# date_of_shots = os.path.basename(os.getcwd()).split(split_character)[0]
date_of_shots = os.path.basename(os.getcwd())
rawfile_path = './'+date_of_shots+'_'+'rawfiles'
rawfile_extention = '.CR2'
jpegfile_extention = '.JPG'
filelist = os.listdir('.');

# method 1-a: Not cross-platform & can't catch error occuring when creating the directory
# if not os.path.exists(rawfile_path):
#     os.makedirs(rawfile_path)

# method 1-b
try:
    os.makedirs(rawfile_path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

# method 1-c: only for Python >= 3.2, but would be removed in 3.4 due to thread-unsafety
# os.makedirs(rawfile_path,exist_ok=True)

# Step 2: move all raw files
jpegfilelist = []

for item in filelist:
    if item.endswith(rawfile_extention):
        shutil.move(item, rawfile_path)
    if item.endswith(jpegfile_extention):
        jpegfilelist.append(item)

# Step 3: create a list of the rawfiles having no corresponding jpeg file, and then remove them
rawfilelist = os.listdir(rawfile_path)
os.chdir(rawfile_path)

for jpegfile in jpegfilelist:
    thefile = os.path.basename(jpegfile).rsplit('.',1)[0]+rawfile_extention
    if thefile in rawfilelist:
        rawfilelist.remove(thefile)

for leftover in rawfilelist:
    # FIXED: ignore the directories under rawfile_path
    if os.path.isdir(leftover):
        continue
    os.remove(leftover)
