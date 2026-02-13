#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())
#./upcase_it.py | cat -e
#./upcase_it.py "initiation" | cat -e

