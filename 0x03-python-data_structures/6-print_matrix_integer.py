#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    for l in matrix:
        for item in l:
            print("{:d}".format(item), sep = ' ', end='')
        print('')
