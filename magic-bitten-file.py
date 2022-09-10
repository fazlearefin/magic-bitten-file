#!/usr/bin/env python3

import argparse
import sys

FILE_SIGNATURES_HEX = {
    "bmp": [0x42, 0x4D],
    "bz2": [0x42, 0x5A, 0x68],
    "gif": [0x47, 0x49, 0x46, 0x38, 0x37, 0x61],
    "gz": [0x1F, 0x8B],
    "ico": [0x00, 0x00, 0x01, 0x00],
    "jpg": [0xFF, 0xD8, 0xFF, 0xE0],
    "mp3": [0xFF, 0xFB],
    "pdf": [0x25, 0x50, 0x44, 0x46, 0x2D],
    "png": [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A],
    "rar": [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x01, 0x00],
    "tar": [0x75, 0x73, 0x74, 0x61, 0x72, 0x00, 0x30, 0x30],
    "tif": [0x49, 0x49, 0x2A, 0x00],
    "zip": [0x50, 0x4B, 0x03, 0x04],
}

def prepend_magic_byes(filename,filetype):
    try:
        # check if the file already has the magic bytes of intended type
        with open(filename, "rb") as file:
            signature = file.read(len(FILE_SIGNATURES_HEX[filetype]))
            if signature == bytes(FILE_SIGNATURES_HEX[filetype]):
                print(f"This file {filename} is already of type {filetype}")
                return None

        with open(filename, "rb+") as file:
            content = file.read()
            file.seek(0)
            file.write(bytes(FILE_SIGNATURES_HEX[filetype]))
            file.write(content)
    except Exception as e:
        sys.exit(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set file options")
    parser.add_argument("-f", "--filetype", required=True, choices=[key for key in FILE_SIGNATURES_HEX], help="Insert magic bytes of this file type")
    parser.add_argument("filename", type=str, help="the filename")
    args = parser.parse_args()

    if args.filetype:
        prepend_magic_byes(args.filename, args.filetype)
