# 3.调试和性能优化
# TODO:

import sys
import traceback
import unittest

""" 3.1定制调试信息
    3.1.1 打印文件名和行号
    借助sys.exc_info 模块自己捕获异常，来打印调用者信息，
    同时打印当前调试信息。
"""
def func_3_1_1():
    def xprint(msg=""):
        try:
            print("do try")
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back

        print('{}[{}]: {}'.format(f.f_code.co_filename, str(f.f_lineno), msg))

    def test_xprint():
        xprint()
        xprint("%d %s" %(10, "hello"))
    
    test_xprint()


""" 3.1.2. 异常时打印函数调用栈
    异常发生时，Python默认处理方式将中断程序的运行,有时候我们希望程序继续运行。
    可以通过 try 语句结合 sys.exc_info() 和 traceback模块抛出异常，并给出提示信息。
"""
def func_3_1_2():
    def divide0(a, b):
        return a / b

    def xtry(runstr):
        ret, status = None, True
        try:
            ret = eval(runstr)
        except:
            info = traceback.format_exc()
            try:
                raise Exception
            except:
                f = sys.exc_info()[2].tb_frame.f_back

            print('%s[%s]: %s' % (f.f_code.co_filename, str(f.f_lineno), info))
            status = False
        return status, ret

    status, ret = xtry("divide0(100, 0)")
    print(status, ret)
    print("still running!!") # 继续执行


""" 3.2. 断言和测试框架
    3.2.1. assert 语句
    assert 在表达式为假时抛出断言异常 AssertionError 并终止程序的执行
"""
def func_3_2_1():
    # AssertionError
    assert 1 == 2
    assert isinstance('str', str)   
    # assert支持一个格式化字符串参数，以逗号区分，用于提供更明确的断言信息
    oct_num = -1
    assert oct_num in range(10), "Oct number must be in (%d-%d)" % (0, 9)
    # out = AssertionError: Oct number must be in (0-9)


""" 3.2.2. 单元测试模块 unittest
    Python 自带单元测试框架 unittest
"""
# unittest测试用例
class test_suit1(unittest.TestCase):
    def test1(self):
        self.assertEqual(1, 1)

class test_suit2(unittest.TestCase):
    def test2(self):
        self.assertEqual(2, 0)

# uncomment bellow when testing, equal to: python -m unittest unit_sample.py
# unittest.main()


# unittest 测试套件
class TestMathFunc(unittest.TestCase):
    def test_abs(self):
        """Test method abs()"""
        self.assertEqual(1, abs(-1))
        self.assertEqual(1, abs(1))
    
    # skip修饰器跳过测试用例
    @unittest.skip("Don't run it now!")
    def test_max(self):
        """Test method max(x1,x2...)"""
        self.assertEqual(2, max(1, 2))

    def test_min(self):
        """Test method min(x1,x2...)"""
        self.assertEqual(1, min(1, 2))

    # 重写setUp() 和 tearDown() 两个方法
    def setUp(self):
        print("Prepare unittest environment.")

    def tearDown(self):
        print("Clean up unittest environment.")
    
    # 想要在所有测试用例执行之前和结束之后，只执行一次准备和清理动作，
    # 可以用 setUpClass() 与 tearDownClass()。
    @classmethod
    def setUpClass(cls):
        print("Prepare unittest environment.")

    @classmethod
    def tearDownClass(cls):
        print("Clean up unittest environment.")



if __name__ == "__main__":
    # func_3_2_1()


    #####test code for TestMathFunc, uncomment when needed#####
    # 创建测试套件
    suite = unittest.TestSuite()
    # 1. 添加部分测试用例
    tests = [TestMathFunc("test_max"), TestMathFunc("test_min")]
    suite.addTests(tests)
    # 2. 添加所有测试用例
    suite.addTest(unittest.makeSuite(TestMathFunc))
    # verbosity 参数可以控制执行结果的输出：0 是简单报告，1 是一般报告，2 是详细报告。
    runner = unittest.TextTestRunner(verbosity=2) # verbosity=0-2 调整输出
    runner.run(suite)

    # print out to txt file
    # suite.addTest(unittest.makeSuite(TestMathFunc))
    # with open('unittest_report.txt', 'w') as f:
    #     runner = unittest.TextTestRunner(stream=f, verbosity=1)
    #     runner.run(suite)
    #####test code for TestMathFunc, uncomment when needed#####
