#!/usr/bin/env python3
# coding=utf-8

"""
基础概念
"""

# variable 变量
# reference 引用，指向内存的一小块

# 将 'Hello World!' 赋值给 变量s
# 常量-字符串
s = 'Hello World!'
# 打印 s
print(s)

# 常量-逻辑值
a = True
b = False
print(a, b)
# a 且 b, a 或 b
print(a and b, a or b)

# 常量-数值, 把2和3分别赋值给a和b
a, b = 2, 3
# if 后面跟一个条件表达式(单独的常量或变量是最简单的表达式)
if a + b > a * b:
    print('if   a + b > a * b')
    # formatted string, 格式化的字符串，可以在字符串中使用变量
    print(f"{a} + {b} > {a} * {b}")
# else if, 否则如果
elif a + b < a * b:
    print('elif a + b < a * b')
    print(f"{a} + {b} < {a} * {b}")
else:
    print('else a + b = a * b')
    print(f"{a} + {b} = {a} * {b}")

# 数值赋值
s = 1
print(s, s * s)
s = s + 1
print(s, s * s)
s = s * 2
print(s, s * s)

s = 0
s = s + 1
s = s + 2
s = s + 3
print(s)

# range返回一个范围，range(n)即返回从 0 到 n-1
# 从 0 到 9
r = range(10)
print(list(r))
print(list(range(1, 101)))

# 遍历(循环语句中的一种)
s = 0
for i in range(1, 101):
    s = s + i
    print(i, s)

# 执行入口，当前文件被执行的时候，才会运行
if __name__ == '__main__':
    print(__name__)

# 导入math模块
import math

print(math.pi)
print(math.e)
print(math.sin)
print(math.sin(math.pi / 2))

# 从math模块导入sin函数和pi常量
from math import sin, cos, tan, pi

print(pi)
print(sin)
print(sin(pi / 2))
print((cos(1) + sin(pi - 1)) * tan(pi / 4))

print(1.01 ** 100)
# power, 幂函数power(a, p) 即a的p次幂
print(math.pow(1.01, 100))
