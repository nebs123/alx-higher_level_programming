#!/usr/bin/python3
def weight_average(my_list=[]):
    weighted_score = sum(map(lambda x: x[0] * x[1], my_list))
    weights = sum(map(lambda x: x[1], my_list))
    if weights == 0:
        return 0
    else:
        return weighted_score / weights
