#!/usr/bin/python3

for i in range (0,26):
    if (ord('a') + i) == ord('q') or (ord('a') + i) == ord('e'):
        continue
    else:
        print("{}".format(chr(ord('a')+ i)), end='')
    
