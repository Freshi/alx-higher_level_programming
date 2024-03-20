#!/usr/bin/python3
def add_tuple(tuple_1=(), tuple_2=()):
    new_tuples = []
    tuples = [tuple_1, tuple_2]
    for item in tuples:
        size = len(item)
        if size == 0:
            new_tuples.append((0, 0))
        elif size == 1 and item[0]:
            new_tuples.append((item[0], 0))
        elif size == 1 and item[1]:
            new_tuple.append((0, item[1]))
        elif size > 2:
            new_tuples.append(item[0:2])
        else:
            new_tuples.append(item)
    a, b = new_tuples
    return tuple(map(sum, zip(a, b)))
