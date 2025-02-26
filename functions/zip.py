import os
import pathlib
import zipfile

from functions.encrypt import encrypt
from functions.compression import decompress
from functions.decompile import decompile

def extract(path, new_name):
    if zipfile.is_zipfile(new_name):
        print("Is a zip file!")

        with zipfile.ZipFile(new_name, 'r') as zip:
            zip.extractall(new_name + "-extracted")
        decompile(new_name + "-extracted")
        decompress(new_name + "-extracted")

    else:
        print("ERROR: Not a zip file")
        print(new_name)
        print(path)

def zip_files(folder_name, new_name):
    folder = pathlib.Path(folder_name)
    split = new_name.split(".")
    file_name = split[0]
    with zipfile.ZipFile(f"{file_name}-unencrypted.shpac", 'w', zipfile.ZIP_STORED) as zip:
        for file in folder.rglob("*"):
            print(file)
            if not file.is_dir():
                arcname = file.relative_to(folder)
                info = zipfile.ZipInfo(str(arcname))
                if file.name.endswith(".json") or file.name.endswith(".bmp"):
                    info.comment = b'z'
                else:
                    info.comment = b''
                with file.open('rb') as f:
                    zip.writestr(info, f.read())

def turn_to_shpac(folder, new_name):
    zip_files(folder, new_name)
    split = new_name.split(".")
    file_name = split[0]
    encrypt(open(f"{file_name}-unencrypted.shpac", 'rb'), open(f"{file_name}.shpac", 'wb'))
    os.remove(f"{file_name}-unencrypted.shpac")