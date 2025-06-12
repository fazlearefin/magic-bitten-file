# magic bitten file

## Purpose

The Python script **`magic_bitten_file.py`** allows you to insert magic bytes of selected file types at the beginning of a malicious file (such as a webshell). This enables the file to bypass file content checks when uploaded to a vulnerable web server, allowing it to be executed.

## Usage

This Python script requires only the Python Standard Library. To use it, simply execute the script.

```console
$ # Create a PHP file
$ printf "%s\n" "<?php phpinfo(); ?>" > code.php

$ # Check what this file is detected as by the Linux file utility
$ file code.php
code.php: PHP script, ASCII text

$ # Make this file appear as a GIF file
$ python3 magic_bitten_file.py -f gif code.php

$ # Check what the Linux file utility now detects this file as
$ file code.php
code.php: GIF image data, version 87a, 16188 x 26736
```

## Alternatives

Instead of using this script, you can take any sample file of your choice from the internet or your local filesystem and append the code to the end of it. However, I found this approach inconvenient during CTFs. This tool simplifies the process by running a single Python script.

Here's a Bash/Zsh one-liner to make a PHP file appear as a GIF file:

```bash
echo -n -e '\x47\x49\x46\x38\x37\x61' | cat - /path/to/php-webshell.php > image.gif
```

---

## Donations

If my work has saved you time and effort, I would appreciate any donation. However, the code in this repository is completely free.

Bitcoin (BTC): `bc1qzlhpm94vtk2ht67etdutzcy2g5an5v6g36tp0m`