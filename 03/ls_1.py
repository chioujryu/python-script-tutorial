'''
Usage:

$ python ls.py sample/
lorem.md
realpython.md
hello.txt

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
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("path")

args = parser.parse_args()

target_dir = Path(args.path)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)