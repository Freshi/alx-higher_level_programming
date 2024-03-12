#!/usr/bin/python3
for n in range(100):
    if n != 99:
        print(f'{n:0=2d}, ', end='')
    else:
        print(f'{n:0=2d}')
