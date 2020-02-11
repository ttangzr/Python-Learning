
def func_2_3():
    # 分隔符打印多个字符串
    str0 = "123"
    str1 = "456%s" # 字符串中的%s不会被解释为格式化字符串

    # 含有%s的格式化字符串只能有一个，且位于最后
    print(str0,str1,"%s%s" %("end", "!"))
    print(str0,str1,"%s%s" %("end", "!"), sep='*')

    print("%s*%s*end!" % (str0, str1)) # 手动指定分隔符
    

if __name__ == "__main__":
    func_2_3()