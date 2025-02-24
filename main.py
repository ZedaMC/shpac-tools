import sys

from functions.decrypt import decrypt, decrypt_and_decompile, verify
from functions.encrypt import encrypt, encrypt_and_compile
from key import AES_KEY, AES_IV

def print_usage(file):
    print(f'Usage: {file} verify/encrypt/decrypt/decrypt_and_decompile infile outfile')
    sys.exit(1)

def main(argc, argv):
    if argc < 3:
        print_usage(argv[0])

    print(argc)
    print(argv)
    if len(AES_KEY) != 16 or len(AES_IV) < 12:
        print('Error: Update AES_KEY and AES_IV in key.py')
        sys.exit(1)

    f = open(argv[2], 'rb')

    if argv[1] == 'verify':
        verify(f)
    elif argv[1] == 'encrypt':
        if argc < 4:
            print_usage(argv[0])
        encrypt(f, open(sys.argv[3], 'wb'))
    elif argv[1] == 'encrypt_and_compile':
        # TODO
        if argc < 4:
            print_usage(argv[0])
        encrypt_and_compile(f, open(sys.argv[3], 'wb'), sys.argv[2], sys.argv[3])
    elif argv[1] == 'decrypt_and_decompile':
        if argc < 4:
            print_usage(argv[0])

        decrypt_and_decompile(f, open(sys.argv[3], 'wb'), sys.argv[3], sys.argv[2])
    elif argv[1] == 'decrypt':
        if argc < 4:
            print_usage(argv[0])
        decrypt(f, open(sys.argv[3], 'wb'))
    f.close()

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)

