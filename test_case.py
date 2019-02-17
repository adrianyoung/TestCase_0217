# -*- coding: utf-8 -*-

import unittest
from no_name_ import no_name_
from max_ import max_

class TestFunc(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_name_(self):

        # 空字符串
        self.assertTrue(no_name_('',''))
        self.assertFalse(no_name_('','abbc'))
        # 同构乱序
        self.assertTrue(no_name_('cabb','abbc'))
        # 异构长度相等
        self.assertFalse(no_name_('cabd','abbc'))
        # 长度不等
        self.assertFalse(no_name_('cabbdd','abbc'))

    def test_max_(self):

        # 默认
        self.assertEqual(max([], default=0), max_([], default=0))
        # 多参数
        self.assertEqual(max(1, 3, -9), max_(1, 3, -9))
        # 支持浮点
        self.assertEqual(max(1.0, 3, -9), max_(1.0, 3, -9))
        # 单参数可迭代对象
        self.assertEqual(max((1, 3, -9)), max_((1, 3, -9)))
        self.assertEqual(max([1, 3, -9]), max_([1, 3, -9]))
        self.assertEqual(max([1, 3, -9], [1, 2, -4]), max_([1, 3, -9], [1, 2, -4]))
        self.assertEqual(max({'a':1, 'b':3, 'c':-9}), max_({'a':1, 'b':3, 'c':-9}))
        # 前置处理
        self.assertEqual(max(1, 3, -9, key=abs), max_(1, 3, -9, key=abs))
        dic = {'a':1, 'b':3, 'c':-9}
        self.assertEqual(max(dic, key=dic.get), max_(dic, key=dic.get))
        # 字符比较
        self.assertEqual(max('139'), max_('139'))
        self.assertEqual(max('abc'), max_('abc'))
        # 稳定性
        a =  ['a']
        b1 = ['a', 'b']
        b2 = ['a', 'b']
        self.assertNotEqual(id(b1), id(b2))
        self.assertEqual(id(max(a, b1, b2)), id(b1))
        self.assertEqual(id(max_(a, b1, b2)), id(b1))
        # 捕捉异常
        # 无参数
        self.assertRaisesRegexp(TypeError,"expected 1 arguments, got 0",max_)
        # 无效参数
        self.assertRaisesRegexp(TypeError,"is an invalid keyword argument for this function", max_, 1, 3, -9, keys=abs)
        # 单参数对象为空
        self.assertRaisesRegexp(ValueError,"arg is an empty sequence", max_, [])
        # 单参数对象不可迭代
        self.assertRaisesRegexp(TypeError,"object is not iterable", max_, 1)
        # 前置方法无效
        self.assertRaisesRegexp(TypeError,"object is not callable", max_, 1, 3, -9, key=1)
        # 多参数不可设置默认
        self.assertRaisesRegexp(TypeError,"Cannot specify a default for .+ with multiple positional arguments", max_, 1, 3, -9, default=0)

if __name__ == "__main__":

    suite = unittest.TestSuite()

    suite.addTest(TestFunc("test_no_name_"))
    suite.addTest(TestFunc("test_max_"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

    # with open('test_report.txt', 'w') as fp:
    #     runner = unittest.TextTestRunner(stream=fp, verbosity=2)
    #     runner.run(suite)


