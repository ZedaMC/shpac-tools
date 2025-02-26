import json

import msgpack
import zstandard

from functions.other import find_all_json_files, find_all_bmp_files

files_list = []

def decompress(folder):
    for item in find_all_json_files(folder):
        try:
            print(item)
            with open(f"{item}", 'rb') as f:
                data = f.read()
                f.close()
            dctx = zstandard.ZstdDecompressor()
            decompressed = dctx.decompress(data)
            decoded = json.loads(decompressed.decode('utf-8'))
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
        with open(f"{item}", 'rb') as f:
            data = f.read()
            f.close()
        dctx = zstandard.ZstdDecompressor()
        decompressed = dctx.decompress(data)
        with open(f"{item}", 'wb') as f:
            f.write(decompressed)
            f.close()
def compress(folder):
    for item in find_all_json_files(folder):
        try:
            print(f"{item}")
            with open(f"{item}", 'r', encoding='utf-8') as f:
                data = json.load(f)
                f.close()
            name = item.name
            if name == 'desc.json':
                    # Turn into a msg pack
                print("Encoding into msgpack format")
                data = msgpack.packb(data)
            else:
                data = json.dumps(data, ensure_ascii=False).encode('utf-8')
            # Compress into ZSTD
            print("Compressing into ZSTD format for " + f"{item}")
            cctx = zstandard.ZstdCompressor()
            compressed = cctx.compress(data)
        except:
            print("Trying method 2")
            with open(f"{item}", 'r', encoding='utf-8') as f:
                data = f.read()
                f.close()
            json_bytes = json.dumps(data).encode('utf-8')
            cctx = zstandard.ZstdCompressor()
            compressed = cctx.compress(json_bytes)
        with open(f"{item}", 'wb') as f:
            f.write(compressed)
            f.close()
    for item in find_all_bmp_files(folder):
        with open(item, 'rb') as f:
            data = f.read()
            f.close()
        print(item)
        cctx = zstandard.ZstdCompressor()
        compressed = cctx.compress(data)
        with open(f"{item}", 'wb') as f:
            f.write(compressed)
            f.close()

