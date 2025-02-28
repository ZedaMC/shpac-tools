# Shpac Tools
Using this project you can easily verify,encrypt and decrypt shpac files. You can also convert a folder to a valid shpac file and also turn a shpac file into a folder. Based off ciphtool by GaryOderNicht. Works with Nintendo Alarmo.

Usage: python main.py verify/encrypt/encrypt_and_compile/homebrew_compile/decrypt/decrypt_and_decompile/homebrew_decompile infile outfile

NOTICE: Unluac may incorrectly decompile some files.

# Setting up
1. Clone the repository
2. Install these packages: `pip install msgpack zstandard pycryptodome pathlib`
3. Download unluac (https://sourceforge.net/projects/unluac/files/Unstable/)
4. Rename the jar to unluac.jar and put in in the tools folder
5. In key.py enter your Alarmo's AES_KEY and AES_IV.
6. In compiling.py specify the lua path.

# Requirements
- Python 3

# TODO
- ~~Encrypt and compile~~
- Config
- Audio file support when decompiling and compiling (Converter)
- Png files are converted to bmp files (Converter)
- MSBT files (for now use https://github.com/IcySon55/3DLandMSBTeditor)
# Credits
GaryOderNichts - Ciphtool https://github.com/GaryOderNichts/alarmo/blob/main/usb_payload/ciphtool.py
Nintendo Alarmo Hacking Discord server - Got a lot of help there when creating the program https://discord.gg/fc8nXpB5eB
