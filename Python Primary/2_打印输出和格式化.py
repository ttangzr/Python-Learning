# 2. 打印输出和格式化
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
# TODO:2.8

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
    """


if __name__ == "__main__":
    func_2_7()