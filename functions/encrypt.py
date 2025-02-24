import pathlib

from Crypto.Cipher import AES

from functions.decrypt import get_remaining_size
from key import AES_KEY, AES_IV


def encrypt_and_compile(f, outf, folder_name, file):
    folder = pathlib.Path(folder_name)

def encrypt(f, outf):
    # Get size to encrypt
    size = get_remaining_size(f)

    # Add file signature
    outf.write(b'CIPH\x00\x00\x00\x00')

    cipher = AES.new(AES_KEY, AES.MODE_CTR, nonce=AES_IV[:12])
    while size > 0:
        to_read = min(size, 0x10000)

        # Encrypt and write to file
        outf.write(cipher.encrypt(f.read(to_read)))
        size -= to_read

    # Add dummy signature
    outf.write(b'\x00' * 0x100)

    outf.close()