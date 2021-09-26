#!/usr/bin/env python3
# coding=utf-8

"""
类型系统
"""

s = 'Hello World!'
# 返回变量s的类型
# type函数：返回指定引用的类型，type(x)即返回x的类型
t = type(s)
# 打印 t
print(t)

print(type)
print(type(type), type(str))
print(type(type(type(type(type)))))

print('1' + '2')
print(1 == '1', 1 == 1)
# int 把任何对象转换为整数
print(int('1'), int('1') == '1', int('1') == 1)
print(type(1) == int, type('1') == str, type(int('1')) == int)
# str 把任何对象转换为字符串
# type 返回对象的类型， 其中type的类型就是其本身
print(str(1) == '1', type(str(1)) == str, type(int) == type, type(type) == type)
# bool 布尔类型，有且只有两个值，即True和False
print(type(True), type(False) == bool, bool('1'), bool(1),
      bool(0), bool('0'), bool(''))
# float 浮点类型(实数类型)
print(type(3.14), type(3.14) == float, type(float(1)) == float,
      type(int(3.14)) == int)

# list 列表类型，多个有序值的集合
s = [1, 2, 3]
print(s, type(s), type(s) == list)
# list作为函数的时候，作用是把对象转换为列表
print(range(1, 4), type(range(1, 4)), type(range(1, 4)) == range,
      list(range(1, 4)) == s)
# 数值0，空字符串，空列表等含有零或空的意思的值转换为bool时，都会转为False
print([], type([]) == list, bool([]), bool([1]))
# len，返回对象的长度(length)，比如字符串的字符数，列表的元素个数等
print(len([]), len(['1']), len([True, 3.14]), len(['', 1, [], 0.0]))
print(len(''), len('a'), len('abc'), len('3.14'))
print(len(['']), len(['a']), len(['abc']), len(['3.14']), len([3.14]))

# None 空类型
print(None, type(None), bool(None))

# 空值作为条件表达式
if None:
    print('None')
elif 0:
    print('0')
elif 0.0:
    print('0.0')
elif '':
    print("''")
elif []:
    print('[]')
elif False:
    print('False')
else:
    print('else')
