from Crypto.Cipher import AES
from key import AES_KEY, AES_IV

from functions.compression import compress


def encrypt_and_compile(folder_name, file_name):
    compress(folder_name)
    # Circular import
    from functions.zip import turn_to_shpac
    turn_to_shpac(folder_name, file_name)

def encrypt(f, outf):
    # Get size to encrypt
    from functions.decrypt import get_remaining_size
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