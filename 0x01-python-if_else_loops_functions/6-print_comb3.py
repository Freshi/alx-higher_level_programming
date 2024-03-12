#!/usr/bin/python3
for n in range(1, 99):
    if n % 11 == 0:
        continue
    elif n <= int(str(n)[::-1]) and int(str(n)[::-1]) < 98:
        print('{:0=2d}, '.format(n), end='')
print(f'{int(str(n)[::-1])}')
