import os, argparse
from os import rename, listdir
from random import randint

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="Path to image folder")
ap.add_argument("-s", "--separator", default="_", help="Char used to separate the filename and the numbers")
ap.add_argument("-d", "--digits", default=5, help="Number of digits to add to filename")
args = vars(ap.parse_args())
path = str(args["path"])
sep_char = str(args["separator"])
num_digits = int(args["digits"])

# Determined digits number generator
def num_generator():
    a = []
    for value in range (0, num_digits):
        value = str(randint(0, 9))
        a.append(value)
        ran_num = "".join(a)
    return(ran_num)

for filename in os.listdir(path):
    ext = filename.split(".")
    g = filename.replace(ext[1], "")
    z = g.replace(".", "")

    add_num = str (z + sep_char + num_generator() + "." + ext[1])
    
    src =f"{path}/{filename}"
    add_num =f"{path}/{add_num}"
         
    # Rename all files
    os.rename(src, add_num)