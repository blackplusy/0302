#coding=utf-8
import  unittest
from test2.test_mathfunc import TestMathFunc

if __name__=='__main__':
    suite=unittest.TestSuite()
    #添加测试用例，顺序是按照我们添加进suite顺序执行
    tests=[TestMathFunc("test_add"),TestMathFunc("test_divide")]
    #添加测试用例到suite中
    suite.addTests(tests)
    #执行测试
    runner=unittest.TextTestRunner(verbosity=2)
    #0 静默模式 只能获得总的测试用例数量和结果，比如 总共1000个，失败20，成功80
    #1 默认模式 类似于静默模式，知识再每个成功的用例前面有个.,每个失败用例前面有个F
    #2 详细模式 测试结果会显示每个用例的所有相关信息
    runner.run(suite)
