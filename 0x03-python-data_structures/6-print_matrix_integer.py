#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    for l in matrix:
        for item in l:
            print("{}".format(item), sep = ' ', end='')
        print('')