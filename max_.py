# -*- coding: utf-8 -*-
def max_(*args, **kwargs):

    # 无参数报错
    if len(args) == 0:
        raise TypeError("max_ expected 1 arguments, got 0")

    # 无效参数报错
    for key in kwargs.keys():
        if key not in ('key', 'default'):
            raise TypeError("'{}' is an invalid keyword argument for this function".format(key))

    # 参数数量为一
    if len(args) == 1:
        src = args[0]
        # 对象不可迭代
        if not hasattr(src, '__iter__'):
            raise TypeError("'{}' object is not iterable".format(str(type(src)).split("'")[1]))
        # 对象为空
        if len(src) == 0:
            if 'default' in kwargs.keys():
                return kwargs['default']
            else:
                raise ValueError("max_() arg is an empty sequence")
        # 执行前置处理
        if 'key' in kwargs.keys():
            func = kwargs['key']
            if hasattr(kwargs['key'], '__call__'):
                if isinstance(src, dict):
                    obj = { e:func(e) for e in src.keys() }
                    idx = dic_check(obj)
                    return idx
                else:
                    obj = [ func(e) for e in src ]
                    idx = iter_check(obj)
                    return src[idx]
            else:
                raise TypeError("'{}' object is not callable".format(str(type(func)).split("'")[1]))
        # 不执行前置处理
        else:
            if isinstance(src, dict):
                obj = src.keys()
                idx = key_check(obj)
                return idx
            else:
                idx = iter_check(src)
                return src[idx]

    # 参数数量多于一
    if len(args) >= 2:
        src = args
        # 不可设置默认最大值
        if 'default' in kwargs.keys():
            raise TypeError("Cannot specify a default for max_() with multiple positional arguments")
        # 执行前置处理
        if 'key' in kwargs.keys():
            func = kwargs['key']
            if hasattr(kwargs['key'], '__call__'):
                obj = [ func(e) for e in src ]
                idx = iter_check(obj)
                return src[idx]
            else:
                raise TypeError("'{}' object is not callable".format(str(type(func)).split("'")[1]))
        # 不执行前置处理
        else:
            idx = iter_check(src)
            return src[idx]

# 字典查询处理
def dic_check(obj):
    for cnt, key in enumerate(obj.keys()):
        if cnt == 0:
            val = obj[key]
            idx = key
        else:
            if obj[key] > val:
                idx = key
    return idx

# 键值查询处理
def key_check(obj):
    for cnt, key in enumerate(obj):
        if cnt == 0:
            val = key
        else:
            if key > val:
                val = key
    return val

# 字符串查询处理
def iter_check(obj):
    idx = 0
    for pos in range(len(obj)-1):
        if obj[pos+1] > obj[pos]:
            idx = pos+1
    return idx

