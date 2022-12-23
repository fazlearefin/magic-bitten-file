#!/usr/bin/env python3

import argparse
import sys

FILE_SIGNATURES_HEX = {
    "bz2": [0x42, 0x5A, 0x68],
    "gif": [0x47, 0x49, 0x46, 0x38, 0x37, 0x61],
    "gz": [0x1F, 0x8B],
    "jpg": [0xFF, 0xD8, 0xFF, 0xE0],
    "mp3": [0xFF, 0xFB],
    "pdf": [0x25, 0x50, 0x44, 0x46, 0x2D],
    "rar": [0x52, 0x61, 0x72, 0x21, 0x1A, 0x07, 0x01, 0x00],
    "tif": [0x49, 0x49, 0x2A, 0x00],
    "png": [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52],
}


def prepend_magic_bytes(filename, filetype):
    try:
        # check if the file already has the magic bytes of intended type
        with open(filename, "rb") as file:
            signature = file.read(len(FILE_SIGNATURES_HEX[filetype]))
            if signature == bytes(FILE_SIGNATURES_HEX[filetype]):
                raise Exception(f"This file {filename} is already of type {filetype}")

        with open(filename, "rb+") as file:
            content = file.read()
            file.seek(0)
            file.write(bytes(FILE_SIGNATURES_HEX[filetype]))
            file.write(content)
    except Exception as exception:
        sys.exit(exception)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set file options")
    parser.add_argument(
        "-f",
        "--filetype",
        required=True,
        choices=list(FILE_SIGNATURES_HEX),
        help="Insert magic bytes of this file type",
    )
    parser.add_argument("filename", type=str, help="the filename")
    args = parser.parse_args()

    if args.filetype:
        prepend_magic_bytes(args.filename, args.filetype)
