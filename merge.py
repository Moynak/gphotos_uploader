import os
import re
from os.path import isfile, join, isdir
import shutil

def getCount(mypath):
    count = 0
    for f in os.listdir(mypath):
        if(isfile(join(mypath, f))):
            count += 1
    return count


def getNewName(file, offset):
    digit = int("".join(filter(str.isdigit, file)))
    # digit = re.findall('\d+', file)
    new_digit = digit + offset
    new_file = file.replace(str(digit), str(new_digit))
    return str(new_file)

def getSubDir(dirname):
    for f in os.listdir(dirname):
        if(isdir(join(dirname, f))):
            return str(join(dirname, f))
    return None

def rename_files(dir_name, offset):
    for file in os.listdir(dir_name):
        if(isfile(join(dir_name, file))):
            new_file = getNewName(file, offset)
            file = join(dir_name, file)
            new_file = join(dir_name, new_file)
            os.rename(file, new_file)


def modify_child(curr_dir, offset = 0):
    curr_f_count = getCount(curr_dir) + offset
    sub_dir = getSubDir(curr_dir)
    if sub_dir is not None:
        rename_files(sub_dir, curr_f_count)
        if getSubDir(sub_dir) is not None:
            modify_child(sub_dir, curr_f_count)

def move_child(curr_dir):
    sub_dir = getSubDir(curr_dir)
    if sub_dir is not None:
        move_child(sub_dir)
        for file in os.listdir(sub_dir):
            if(isfile(join(sub_dir, file))):
                shutil.move(join(sub_dir, file), curr_dir)
    
def strips(curr_dir):
    for file in os.listdir(curr_dir):
        if isfile(join(curr_dir, file)):
            new_file = file.lstrip("0")
            os.rename(join(curr_dir, file), join(curr_dir, new_file))


parent_dir = "xyz"

for dir in os.listdir(parent_dir):
    if(isdir(join(parent_dir, dir))):
        dir = join(parent_dir, dir)
        modify_child(dir)
        move_child(dir)
        strips(dir)
