#!/usr/bin/env python3

import argparse
import sys

FILE_SIGNATURES = {
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
    """Print all available file type signatures."""
    print('\n'.join(FILE_SIGNATURES))

def prepend_magic_bytes(filename, filetype):
    """Prepend magic bytes to the file if not already present."""
    try:
        with open(filename, 'rb+') as file:
            # Read only the necessary bytes for signature check
            signature = file.read(len(FILE_SIGNATURES[filetype]))
            if signature == bytes(FILE_SIGNATURES[filetype]):
                sys.exit(f"File {filename} is already of type {filetype}")

            # Reset to start, write signature, then append original content
            file.seek(0)
            content = file.read()  # Read remaining content
            file.seek(0)
            file.write(bytes(FILE_SIGNATURES[filetype]) + content)
    except FileNotFoundError:
        sys.exit(f"File {filename} not found")
    except PermissionError:
        sys.exit(f"Permission denied accessing {filename}")
    except OSError as error:
        sys.exit(f"Error processing {filename}: {error}")

def main():
    """Handle command-line arguments and execute operations."""
    parser = argparse.ArgumentParser(description="Modify file magic bytes")
    parser.add_argument('-f', '--filetype', choices=FILE_SIGNATURES.keys(),
                        help="File type for magic bytes")
    parser.add_argument('-l', '--list', action='store_true',
                        help="List all file signatures")
    parser.add_argument('filename', type=str, nargs='?', help="Target file")
    args = parser.parse_args()

    if args.list:
        list_signatures()
    elif args.filetype and args.filename:
        prepend_magic_bytes(args.filename, args.filetype)
    else:
        if not args.filetype and args.filename:
            sys.exit("Error: --filetype is required when specifying a filename")
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()