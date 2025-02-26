import os

from functions.other import find_all_lua_files


def decompile(folder):
    lua_files = find_all_lua_files(folder)
    for item in lua_files:
        if is_compiled(item):
            print(item)
            new_name = f"{item}-decompiled.lua"
            os.system("java -jar tools/unluac.jar " + f"{item}" + " > " + new_name)
            os.remove(f"{item}")
            os.rename(new_name, f"{item}")

def is_compiled(item):
    try:
        with open(item, 'r', encoding='utf-8') as f:
            data = f.read()
            return False
    except:
        return True
