import pathlib

def find_all_bmp_files(folder_name):
    folder = pathlib.Path(folder_name)
    items = []
    for item in folder.rglob("*.bmp"):
        items.append(item)
    return items

def find_all_json_files(folder_name):
    folder = pathlib.Path(folder_name)
    items = []
    for item in folder.rglob("*.json"):
        items.append(item)
    return items

def find_all_lua_files(folder_name):
    folder = pathlib.Path(folder_name)
    items = []
    for item in folder.rglob("*.lua"):
        items.append(item)
    return items