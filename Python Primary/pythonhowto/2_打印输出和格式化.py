# 2. 打印输出和格式化
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# TODO:

import sys


def func_2_3():
    """分隔符打印多个字符串
    print()函数支持一次输入多个打印字符串，默认以空格分割，可以通过sep参数指定分割符号
    """ 
    
    str0 = "123"
    str1 = "456%s" # 字符串中的%s不会被解释为格式化字符串

    # 含有%s的格式化字符串只能有一个，且位于最后
    print(str0,str1,"%s%s" %("end", "!"))
    print(str0,str1,"%s%s" %("end", "!"), sep='*')

    print("%s*%s*end!" % (str0, str1)) # 手动指定分隔符
    

def func_2_4():
    """格式化输出到变量
    通过打印字符串的 ascii 码，可以看到换行符是 print()函数在打印时追加的，
    而并没有格式化到变量中。
    """
    tmpstr = ("Number is: %d" % 100)
    print(tmpstr)
    hexlist = [("%02x" % ord(x) )for x in tmpstr]
    print(' '.join(hexlist))
    print("end")


def func_2_5():
    """长行打印输出
    有三种形式：分别是加'\'，三引号，每行引号
    """
    def print_long_line1():
        print("The door bursts open. A MAN and WOMAN enter, drunk and giggling,\
horny as hell.No sooner is the door shut than they're all over each other,\
ripping at clothes,pawing at flesh, mouths locked together.")

    def print_long_line2():
        print("""The door bursts open. A MAN and WOMAN enter, drunk and giggling,
horny as hell.No sooner is the door shut than they're all over each other,
ripping at clothes,pawing at flesh, mouths locked together.""")

    def print_long_line3():
        print("The door bursts open. A MAN and WOMAN enter, drunk and giggling,"
            "horny as hell.No sooner is the door shut than they're all over each other,"
            "ripping at clothes,pawing at flesh, mouths locked together.")
    print_long_line1()
    print_long_line2()
    print_long_line3()


def func_2_6():
    # 打印含有引号的字符串
    print('It is a "Gentleman" dog!')
    print("It is a 'Gentleman' dog!")
    print('''It's a "Gentleman" dog!''')


def func_2_7():
    """打印输出到文件
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    file 参数来指定输出文件的描述符，默认值是标准输出sys.stdout
    标准的错误输出是 sys.stderr，当然也可以指定普通文件描述符

    输出到磁盘文件时，为了保证实时性，可能需要把 flush 参数设置为 True。
    """
    logf = open("logfile.log", "a+")
    print("123", file=logf, flush=True)


def func_2_8():
    """对齐输出（左中右对齐）
    1.print()函数左对齐，只能使用默认的空格进行填充
    2.ljust(), rjust() 和 center() 
    """
    # print() 
    man = [["Name", "John"], ["Age", "25"], ["Address", "BeiJing China"]]
    for i in man:
        print("%-10s:%s" % (i[0], i[1]))

    # ljust(), rjust() 和 center() 
    print("123".ljust(5, '*'))
    print("123".rjust(5, '*'))
    print("123".center(5, '*'))


def func_2_9():
    """格式化输出
    1. 百分号格式化（数值格式化、字符串格式化）
    2.format格式化（位置匹配、数值格式转换、位数对齐和补全、千位分割数字
                    时间格式化、占位符嵌套、 repr 和 str 占位符、 format 缩写形式）
    """
    ## % 
    # 数值格式化
    print('%o %d %x %X' % (10, 10, 10, 10))     # out = 12 10 a A
    print('%f' % 1.23)                          # out = 1.230000
    print('%.2f' % 1.23)                        # out = 1.23
    print('%e' % 1.23)                          # out = 1.230000e+00
    print('%.2e' % 1.23)                        # out = 1.23e+00
    # 字符串格式化
    print('%s' % 'hello world')                 # 字符串输出
    print('%10s' % 'hello world')               # 右对齐，取10个字符，不够则空格补位
    print('%-10s' % 'hello world')              # 左对齐，取10个字符，不够则空格补位
    print('%-10.2s' % 'hello world')            # 左对齐，取2个字符

    ## format
    # 位置匹配
    print('{} {}'.format('hello','world'))              # 默认从左到右匹配
    print('{0} {1}'.format('hello','world'))            # 按数字编号匹配
    print('{0} {1} {0}'.format('hello','world'))        # 打乱顺序
    print('{wd} {ho}'.format(ho='hello',wd='world'))    # 关键字匹配

    # object
    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

        # 通过对象属性匹配
        def __str__(self):
            return 'Point({self.x}, {self.y})'.format(self=self)

    print(str(Point(1, 2)))

    a = {'a': 'val_a', 'b': 'val_b'}
    b = a
    print('X: {0[a]};  Y: {1[b]}'.format(a, b))     # out = 'X: val_a;  Y: val_b'
    # 数值格式转换
    print('{:x},{:X}'.format(0xab, 0xab))           # out = ab,AB
    print("int: {0:d};hex: {0:#x};bin: {0:#b}".format(42))      # out = 'int: 42;hex: 0x2a;bin: 0b101010'
    # 位数对齐和补全:< （默认）左对齐、> 右对齐、^ 中间对齐、= （只用于数字）在小数点后进行补齐
    print('{:^10s} and {:^10s}'.format('hello','world')) 
    print('{} is {:.2f}'.format(1.123, 1.123))      # 1.123 is 1.12
    print('{:*^30}'.format('centered'))             # 使用“*”填充
    print('{:0=30}'.format(11))                     # 还有“=”只能应用于数字，这种方法可用“>”代替
    # 正负号
    print('{:+f}; {:+f}'.format(3.14, -3.14))       # 总是显示符号
    print('{: f}; {: f}'.format(3.14, -3.14))       # 若是+数，则在前面留空格
    print('Correct answers: {:.2%}'.format(1/2.1))  # out = 'Correct answers: 47.62%'
    # 千位分割数字
    print('{:,}'.format(1234567890))                # out = '1,234,567,890'
    # 时间格式化
    import datetime
    d = datetime.datetime(2020, 3, 20, 16, 7, 50)   # out = '2020-3-20 16:07:50'
    # 占位符嵌套

    # repr 和 str 占位符
    print("repr() shows quotes: {!r}; str() doesn't: {!s}"
        .format('test1', 'test2'))                  # out = "repr() shows quotes: 'test1'; str() doesn't: test2"
    # format 缩写形式
    print('My salary is {salary:10.2f}')


if __name__ == "__main__":
    func_2_9()