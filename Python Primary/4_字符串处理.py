# 4.字符串处理
# TODO:


def func_4_1():
    # 4.1. 创建字符串变量
    str0 = "Hello"   # 双引号
    str1 = 'world!'  # 单引号
    str2 = """123""" # 三引号
    str3 = '''456'''
    # 多行
    str4 = "hello"\
        "world"
    str5 = """hello\
    world"""

    str6 = str5[:]  # copy

    str7 =  r"123\"\'456"


def func_4_3():
    # 4.3. 访问字符串中的值
    # 切片操作支持指定步长，格式为 [start:stop:step]
    str0 = '0123456789'
    print(str0[1::2]) 

    # 过滤特定的字符 filter(function or None, iterable) –> filter object
    iterable0 = filter(lambda i: int(i)%2 == 0, str0)
    print("".join(iterable0))
    

def func_4_4 ():
    # 4.4. 更新字符串中的值
    # 字符串不能直接修改，只能转换为其他类型更新后在转换回字符串

    # 转换为为list
    str0 = "0123456"
    list0 = list(str0)
    list0[0] = 'a'
    str0 = ''.join(list0)
    print(str0)

    # 切片
    str1 = str0[:3] + 'a' + str0[3:]
    print(str1)


def func_4_5():
    # 4.5. 字符串格式化
    print("%c" % 'a')
    print("%s" % "string")
    print("%s" % 123)   # 自动调用str()转换为str
    print("%d" % 100.0) # 自动调用int()转换为int

    print('%(language)s has %(number)01d quote types.' % {'language': "Python", "number": 2})

    print("{} {}".format("abc", "123"))         # 不指定位置，按默认顺序
    print("name: {name}, age: {age}".format(name="John", age="25"))
    print('{:b}'.format(11))                    # 二进制
    print("{0} is {{0}}".format("value"))       # value is {0}


def func_4_6():
    # 4.6. 字符串查找和统计
    str0 = "01234566"
    print("123" in str0)
    print("123" not in str0)

    # 指定范围查找字符串 
    # S.find(sub [,start [,end]]) -> int
    print(str0.find("78"))
    # S.[rindex]index(sub [,start [,end]]) -> int,找不到时会抛出 ValueError 异常
    print(str0.index("78"))
    # S.endswith(suffix[, start[, end]]) -> bool
    print(str0.endswith("89"))
    # min() max()
    print(max(str0), min(str0))
    # 统计字符串出现次数 S.count(sub[, start[, end]]) -> int
    print(str0.count("0", 0, 9))


def func_4_7():
    # 4.7. 字符串大小写转换
    # 首字符转化为大写 S.capitalize() -> string
    print("a, B".capitalize())
    # 转为大写或小写 S.upper() -> string S.lower() -> string
    str0 = "Hello World!"
    print(str0.upper())
    print(str0.lower())
    # 大小写反转 S.swapcase() -> string
    print(str0.swapcase())
    # 标题化字符串 S.title() -> string
    print(str0.title())


def func_4_8():
    # 4.8. 字符串对齐和填充 S.zfill(width) -> string
    str0 = "Hello world"
    print(str0.zfill(30))
    print(str0.rjust(30, '0'))


def func_4_9():
    # 4.9. 字符串strip和分割 
    # 去除首位空白字符或指定字符串S.strip([chars]) -> string or unicode
    str0 = "  hello  \r\n\t\v\f"
    str1 = "00000hell10o10000"
    print(str0.strip())       # 去除首尾空白符号
    print(str1.strip("01"))   # 去除首尾字符 1和0
    # 如果参数 chars 为 unicode 类型，用lstrip() 和 rstrip() 方法
    # 单次分割
    str0 = "www.google.com"
    print(str0.partition("."))
    # 字符串切片
    str0 = "abcdef \n12345 \nxyz";
    print(str0.split())
    print(str0.split(' ', 1))
    # 按换行符切割
    str0 = 'str1\n\nstr2\n\rstr3\rstr4\r\n\r\n'
    print(str0.splitlines())

def func_4_10():
    # 4.10字符串替换，制表符替换为空格
    str0="s\te"
    print(str0)
    print(str0.expandtabs())
    # 新子串替换旧子串
    str0 = "old old old old"
    print(str0.replace("old", "new"))


def func_4_11():
    # 4.11字符串排序
    str0 = "hello"
    print(''.join(sorted(str0)))


def func_4_12():
    # 4.12. 字符串合并
    str0 = "ABC"
    tuple0 = ("a", "b", "c")
    list0 = ["1", "2", "3"]

    print("--".join(str0))          # a--b--c
    print("--".join(tuple0))        # 1--2--3
    print("--".join(list0))         # A--B--C
    print("".join(list0))           # ABC