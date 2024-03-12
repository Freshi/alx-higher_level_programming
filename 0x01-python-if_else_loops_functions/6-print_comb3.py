#!/usr/bin/python3
for n in range(1,99):
    if n % 11 == 0 and int(str(n)[::-1]) != 97:
        continue
    elif n <= int(str(n)[::-1]) and int(str(n)[::-1]) < 98:
        print(f'{n:0=2d}, ', end='')
print(f'{int(str(n)[::-1])}')
