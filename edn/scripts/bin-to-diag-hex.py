#!/usr/bin/env python3
import sys
if len(sys.argv) != 2:
    sys.exit(-1)
with open(sys.argv[1], "rb") as f:
    print(f"h'{f.read().hex()}'")
