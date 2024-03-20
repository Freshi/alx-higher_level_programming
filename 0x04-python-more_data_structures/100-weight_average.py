#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list):
        get_scores = sum(list(map(lambda x: x[0] * x[1], my_list)))
        get_weights = sum(list(map(lambda x: x[1], my_list)))
        return get_scores/get_weights
    else:
        return 0
