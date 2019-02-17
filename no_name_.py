# -*- coding: utf-8 -*-

# 简洁版
def no_name_(a, b):

    if len(a) != len(b):
        return False

    dict_a = {}
    dict_b = {}
    for x,y in zip(a, b):
        dict_a[x] = dict_a.get(x, 0) + 1
        dict_b[y] = dict_b.get(y, 0) + 1

    return dict_a == dict_b
