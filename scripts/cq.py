#!/usr/bin/env python3
import sys
import cbor2
import re

if 2 <= len(sys.argv) and sys.argv[1] != "--":
    with open(sys.argv[1], "rb") as f:
        data = f.read()
else:
    data = sys.stdin.buffer.read()

cbor = cbor2.loads(data)

if 3 <= len(sys.argv):
    position = sys.argv[2]
else:
    position = "[value]"

while len(position) != 0:
    m = re.match(r"\[(-?\d+|value|tag|wrapped)\]", position)
    if m is None:
        print(f"illegal position: {position}", file=sys.stderr)
        sys.exit(1)

    r = m.groups(1)[0]
    position = position[m.end():]

    if r == "tag":
        if not hasattr(cbor, "tag"):
            print(f"AttributeError: {cbor} does not have any tag", file=sys.stderr)
            sys.exit(1)
        cbor = cbor.tag
        continue

    if hasattr(cbor, "value"):
        cbor = cbor.value
    if r == "value":
        pass
    elif r == "wrapped":
        if not isinstance(cbor, bytes):
            print(f"TypeError: {cbor} is not bstr wrapped value", file=sys.stderr)
            sys.exit(1)
        cbor = cbor2.loads(cbor)
    else:
        if not isinstance(cbor, dict) and not isinstance(cbor, list):
            print(f"TypeError: {cbor} is not map nor array", file=sys.stderr)
            sys.exit(1)
        try:
            cbor = cbor[int(r)]
        except KeyError:
            print(f"KeyError: {cbor} does not have key {r}", file=sys.stderr)
            sys.exit(1)
        except IndexError:
            print(f"IndexError: {cbor} does not have item #{r}", file=sys.stderr)

if cbor is None:
    print("null", end="")
elif isinstance(cbor, bytes):
    print(f"h'{cbor.hex().upper()}'", end="")
else:
    print(cbor, end="")
