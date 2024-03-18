#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lizt in matrix:
        if len(lizt) == 0:
            print('')
            continue
        i, last_idx = 0, len(lizt) - 1
        while (i < last_idx):
            print("{:d} ".format(lizt[i]), end='')
            i += 1
        print(lizt[i])
