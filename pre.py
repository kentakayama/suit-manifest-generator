#!/usr/bin/env python3

import sys
import os
import re
import binascii
import hashlib

def replace_from_pattern(f):
    pat = re.compile(r"(.*)\{\{FILE-(HEX|SIZE|SHA-256) ([~_\./0-9a-zA-Z]+)\}\}(.*)")
    for line in f:
        m = pat.match(line)
        if m:
            pre, op, filename, post = m.groups()
            if "HEX" == op:
                with open(os.path.expanduser(filename), 'rb') as rf:
                    print(pre + rf.read().hex() + post)
            elif "SIZE" == op:
                print(pre + str(os.stat(os.path.expanduser(filename)).st_size) + post)
            elif "SHA-256" == op:
                with open(os.path.expanduser(filename), 'rb') as rf:
                    print(pre + hashlib.sha256(rf.read()).hexdigest() + post)
        else:
            print(line, end="")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            replace_from_pattern(f)
    else:
        replace_from_pattern(sys.stdin)

