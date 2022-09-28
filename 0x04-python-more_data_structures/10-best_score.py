#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        max_key = None
        max = float('-inf')
        for key, value in a_dictionary.items():
            if value > max:
                max = value
                max_key = key
        return max_key
