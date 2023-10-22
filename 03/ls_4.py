'''
Usage:

$ python ls.py -l sample/
  2609 Oct 28 14:07:04 lorem.md
   428 Oct 28 14:07:04 realpython.md
    83 Oct 28 14:07:04 hello.txt

$ python ls.py -h
usage: ls [-h] [-l] path

List the content of a directory

positional arguments:
  path

options:
  -h, --help  show this help message and exit
  -l, --long

Thanks for using ls! :)

$ python ls.py
usage: ls.py [-h] path
ls.py: error: the following arguments are required: path

$ python ls.py sample/ other_dir/
usage: ls.py [-h] path
ls.py: error: unrecognized arguments: other_dir/

$ python ls.py non_existing/
The target directory doesn't exist
'''

import argparse
import datetime
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! :)",
)

parser.add_argument("path")

parser.add_argument("-l", "--long", action="store_true")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime).strftime(
            "%b %d %H:%M:%S"
        )
        return f"{size:>6d} {date} {entry.name}"
    return entry.name

for entry in target_dir.iterdir():
    print(build_output(entry, long=args.long))