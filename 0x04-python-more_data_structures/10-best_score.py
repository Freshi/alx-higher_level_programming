#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_score = max(a_dictionary.values())
        return ''.join({k for k, _ in a_dictionary.items() if _ == best_score})
    else:
        return None
