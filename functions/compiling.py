import os

from functions.other import find_all_lua_files

# Path to Luac
Luac_Path="/home/zeda/Documents/Projects/luac/src/./luac"
errors = []

def decompile(folder):
    lua_files = find_all_lua_files(folder)
    for item in lua_files:
        if is_compiled(item):
            print(item)
            new_name = f"{item}-decompiled.lua"
            os.system("java -jar tools/unluac.jar " + f"{item}" + " > " + new_name)
            os.remove(f"{item}")
            os.rename(new_name, f"{item}")

def compile(folder):
    lua_files = find_all_lua_files(folder)
    for item in lua_files:
        if not is_compiled(item):
            try:
                data = None
                with open(item, 'r') as f:
                    data = f.read()
                print(item)
                new_name = f"{item}-compiled.lua"
                os.system(f"{Luac_Path} -o {new_name} {item}")
                os.remove(f"{item}")
                os.rename(new_name, f"{item}")
            except:
                print(f"Look's like there was an error while compiling. Item: {item}")
                with open(item, 'w') as f:
                    f.write(data)
                errors.append(item)

def is_compiled(item):
    try:
        with open(item, 'r', encoding='utf-8') as f:
            data = f.read()
            return False
    except:
        return True
