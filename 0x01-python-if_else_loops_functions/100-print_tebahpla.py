#!/usr/bin/python3
for alpha in range(ord('z'), ord('A') - 1, -1):
    if alpha % 2 == 0:
        print(chr(alpha).lower(), end="")
    else:
        print(chr(alpha).upper(), end="")
