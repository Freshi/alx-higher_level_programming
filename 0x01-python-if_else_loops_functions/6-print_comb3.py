#!/usr/bin/python3
for n in range(1,99):
    if n % 11 == 0 and int(str(n)[::-1]) != 97:
        continue
    elif n <= int(str(n)[::-1]) and int(str(n)[::-1]) < 98:
        print('{}, '.format(int(str(n)[::-1])), end='')
print(f'{int(str(n)[::-1])}')
