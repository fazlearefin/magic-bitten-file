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

def list_signatures():
    """Prints all the available file type signatures."""
    for filetype in FILE_SIGNATURES_HEX:
        print(filetype)

def prepend_magic_bytes(filename, filetype):
    """Prepends the magic bytes of the specified file type to the given file."""
    try:
        with open(filename, "rb") as file:
            signature = file.read(len(FILE_SIGNATURES_HEX[filetype]))
            if signature == bytes(FILE_SIGNATURES_HEX[filetype]):
                raise ValueError(f"This file {filename} is already of type {filetype}")

        with open(filename, "rb+") as file:
            content = file.read()
            file.seek(0)
            file.write(bytes(FILE_SIGNATURES_HEX[filetype]))
            file.write(content)
    except ValueError as value_error:
        sys.exit(value_error)
    except (OSError, IOError) as error:
        sys.exit(f"Error reading or writing to file {filename}: {error}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set file options")
    parser.add_argument(
        "-f",
        "--filetype",
        choices=list(FILE_SIGNATURES_HEX),
        help="Insert magic bytes of this file type",
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List all the file signatures"
    )
    parser.add_argument("filename", type=str, nargs='?', help="the filename")
    args = parser.parse_args()

    if args.list:
        list_signatures()
    elif args.filetype and args.filename:
        prepend_magic_bytes(args.filename, args.filetype)
    else:
        parser.print_help()
