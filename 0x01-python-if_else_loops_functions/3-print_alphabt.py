#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if chr(x) == 'q' or chr(x) == 'e':
        continue
    print('{}'.format(chr(x)), end="")
