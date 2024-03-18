#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for l in matrix:
        if len(l) == 0:
            print('')
            continue
        i , last_idx = 0, len(l) - 1
        while(i < last_idx):
            print("{:d} ".format(l[i]), end='')
            i += 1
        print(l[i])
