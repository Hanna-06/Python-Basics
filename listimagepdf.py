#Python program to list image, pdf in a folder.

import os
from os import listdir
folder="PATH"
for a in os.listdir(folder):
    if a.endswith(".png" or ".jpg" or ".jpeg"):
        print(a)
    elif a.endswith(".pdf"):
        print(a)
