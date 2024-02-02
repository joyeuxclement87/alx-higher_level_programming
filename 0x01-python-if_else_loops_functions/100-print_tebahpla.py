#!/usr/bin/python3
for a in range(ord('z'), ord('a') - 1, -1):
    if a % 2 == 0:
        dif = 0
    else:
        dif = 32
    print('{}'.format(chr(a - dif)), end='')
