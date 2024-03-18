#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    for list in matrix:
        i , last_idx = 0, len(list) - 1
        while(i < last_idx):
            print("{:d}".format(list[i]), sep=' ', end='')
            i += 1
        print(list[i])
