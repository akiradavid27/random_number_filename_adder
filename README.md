# random_number_filename_adder
This script modifies all filenames of a given folder by adding them a certain number of random digits before the file extension.
# How to use
There are three arguments you can add on the command line interface.
- -p: path to the images folder
- -s: char that will be used to separate the filename and the random digits. (It is set "_" as default).
- -d: specify how many random digits will be added. (It is set "5" as default).

An example could be:
- python Filename_editor.py -p ./train -s - -d 6

# Where to use
You can use this script to rename an image dataset's filenames that will be used to train a Deep Learning model, one example (which I used it for) was the LPRnet model used for OCR implemented in the [bluesy7585/tensorflow_LPRnet](github.com/bluesy7585/tensorflow_LPRnet) repository.
