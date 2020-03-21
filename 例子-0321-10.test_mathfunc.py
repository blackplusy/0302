#coding=utf-8
#把mathfunc中的功能代码导入到当前文件
from test1.mathfunc import *
# from mathfunc import *
import unittest

class TestMathFunc(unittest.TestCase):
    #测试mathfunc.py
    def test_add(self):
        #测试add(a,b)方法
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(4,add(3,2))
    def test_divide(self):
        #测试divide(a,b)
        self.assertEqual(2,divide(6,3))

if __name__=='__main__':
    unittest.main()


