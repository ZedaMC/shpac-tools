import os
import zipfile
import pathlib
from zipfile import is_zipfile

from functions.decompile import decompile
from functions.decompress import decompress


def extract(output, f, path, new_name):
    if is_zipfile(new_name):
        print("Is a zip file!")

        with zipfile.ZipFile(new_name, 'r') as zip_ref:
            zip_ref.extractall(new_name + "-extracted")
            decompile(new_name + "-extracted")
            decompress(new_name + "-extracted")
    else:
        print("ERROR: Not a zip file")
        print(new_name)
        print(path)

def zip(folder, file):
    folder.rglob()