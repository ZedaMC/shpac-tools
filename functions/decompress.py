import pathlib

import zstandard
import json
import msgpack

from functions.other import find_all_json_files, find_all_bmp_files


def decompress(folder):
    for item in find_all_json_files(folder):
        try:
            print(item)
            with open(item, 'rb') as f:
                data = f.read()
            dctx = zstandard.ZstdDecompressor()
            decompressed = dctx.decompress(data)
            decoded = decompressed.decode('utf-8')
            with open(f"{item}", 'w', encoding='utf-8') as f:
                json.dump(decoded, f, ensure_ascii=False, indent=4)
                f.close()
        except:
            print("Trying to decode with msgpack for " + f"{item}")
            decoded_msgpack = msgpack.unpackb(decompressed)
            with open(f"{item}", 'w', encoding='utf-8') as f:
                json.dump(decoded_msgpack, f, ensure_ascii=False, indent=4)
                f.close()
    for item in find_all_bmp_files(folder):
        print(item)
        with open(item, 'rb') as f:
            data = f.read()
        dctx = zstandard.ZstdDecompressor()
        decompressed = dctx.decompress(data)
        with open(f"{item}", 'wb') as f:
            f.write(decompressed)