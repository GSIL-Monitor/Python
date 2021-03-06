# coding=utf-8
"""
函数: 封装具有独立功能的代码块;func表示这是一个函数,func()表示调用这个函数
区别: 方法在类里面,第一个参数默认self;函数在类外面,没有默认参数
"""


def test01(name, gender=True):
    """
    缺省参数: 当某个参数多数情况下都是固定值时就可以设置成缺省参数,比如列表的sort方法(默认升序,指定reverse=Ture才是降序)
    注意: 缺省参数要放在参数列表的末尾
    """
    gender_value = "男生"
    if not gender:
        gender_value = "女生"
    print("%s是%s" % (name, gender_value))


def cumulate(n):
    # 累加案例
    if n == 1:
        return 1
    else:
        return cumulate(n - 1) + n


def fibonacci(n):
    # 菲波那切数列
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def input01():
    # input(): 键盘录入只能输入字符串,数字类型要用int,float等函数转换
    price = float(input("请输入单价:"))
    weight = int(input("请输入重量:"))
    money = price * weight
    print(money)


def eval01():
    # eval(): 可以将input输入的字符串当成有效表达式(取字符串里的内容)并返回计算结果
    result = eval(input("输入算术题:"))
    print(result)


def id01():
    # id(): 可以查看变量在内存中的地址值
    num = 10
    print("%d" % id(num))  # 1537823824 (%d以十进制输出结果)
    print("%x" % id(num))  # 5ba95450 (%x以十六进制输出结果)


def print01():
    """
    print(): 默认换行,在结尾添加end=""可以不换行接着输出
    %表示格式化输出符: 当print函数输出的内容包含多种不同类型的变量,就要对变量进行格式化
    %s:字符串  %d:整数  %f:小数  %%:输出%
    """

    # 格式化输出字符串
    name = "小花"
    print("大家好我叫 %s" % name)  # 大家好我叫 小花

    # 格式化输出整数(06控制长度,不满6位以0补全)
    num = 19
    print("我的学号是 %06d" % num)  # 我的学号是 000019

    # 格式化输出小数(.2控制长度,小数点后面保留2位)
    price = 4.5
    weight = 5
    money = price * weight
    print("苹果单价 %.2f 元/斤,重量 %d 斤,总价 %.2f 元" % (price, weight, money))  # 多个变量放()用逗号隔开

    # 格式化输出百分比
    scale = 0.25
    print("数据比例是 %.2f%%" % (scale * 100))


def high_order():
    """
    高阶函数：一个函数接收另一个函数作为参数
    map(function, sequence)：对sequence中的item依次执行function后将结果组成迭代器返回
    reduce(function, sequence[, initial])：先对sequence中前两个item执行function得到的结果再与下一个item执行function如此迭代
                                           如果有initial则作为初始值调用
    filter(function, sequence)：对sequence中的item依次执行function后将结果值返回True的组成迭代器返回
    """
    from functools import reduce

    res1 = list(map(lambda x: x * x, [1, 2, 3]))
    print(res1)  # [1, 4, 9]
    res2 = reduce(lambda x, y: x + y, [1, 2, 3, 4])
    print(type(res2))
    print(res2)  # 10
    res3 = reduce(lambda x, y: x * y, [1, 2, 3], 5)
    print(res3)  # 30
    res4 = reduce(lambda a, b: a if (a > b) else b, [23, 11, 59, 42, 100])
    print(res4)  # 100
    res5 = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))
    print(res5)  # [2, 4]


if __name__ == '__main__':
    # input01()
    # eval01()
    # id01()
    # print01()
    high_order()
