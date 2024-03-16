#!/usr/bin/python3
def no_c(my_string):
    new_text = []
    for s in my_string:
        if s == 'C' or s == 'c':
            continue
        else:
            new_text.append(s)
    return ''.join(new_text)
