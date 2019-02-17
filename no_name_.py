# -*- coding: utf-8 -*-

# 判断两个字符串是否同构乱序
def no_name(a, b):
    if len(a) != len(b):
        return False

    # 在b中搜索字符串a的首字母
    for x in range(len(b)):
        # 如果命中，删除相同的字符
        if a[0] == b[x]:
            # 比较两个剩余字符串
            return no_name(func(a, 0), func(b, x))

    return len(b) == 0

# 删除指定位置上的一个字符
def func(s, j):
    ret = []
    for k in range(len(s)):
        if (k == j):
            pass
        else:
            ret.append(s[k])
    return ''.join(ret)

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

if __name__ == "__main__":
    a = 'abcab'
    b = 'bbaac'
    print (no_name(a, b))
    print (no_name_(a, b))
