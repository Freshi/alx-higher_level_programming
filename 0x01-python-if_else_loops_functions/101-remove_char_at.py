#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = []
    for i in range(len(str)):
        if i == n:
            continue
        else:
	    str1.append(str[i])
    return ''.join(str1)
