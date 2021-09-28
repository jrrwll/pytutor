#!/usr/bin/env python3
# coding=utf-8

"""
计算器
"""

s = []
t = [1, 2]
s.append(t)
s.append([2, 1])
print(s[0], s[1], s)
x, y = s[0], s[1]
print(x[0], y[1])
print(s[0][0], s[1][1])
print(x[0] == s[0][0], y[1] == s[1][1])

a = []
print(a, len(a))
a.append(a)
print(a, a[0], len(a))
# == 的一般含义为 内存指向是同一个时返回True
print(type(a), type(a[0]), a == a[0])
print(a[0][0][0][0][0][0][0][0][0][0][0][0][0][0])

for i in range(1, 4):
    print(i)
a = list(range(1, 4))
# a为任一可遍历对象，比如range、list、str
for i in a:
    print(i)
for c in 'abc世界':
    print(c)
a = [[11, 12, 13], [21, 22, 23, 24]]
for i in a:
    print(i)
    for j in i:
        print(j)
    print("after")

# 杨辉三角
a=[]
for i in range(0, 6):
    b = []
    a.append(b)
    for j in range(0, 6):
        if i == 0 or j == 0:
            b.append(1)
        else:
            c = a[i-1][j] + a[i][j-1]
            b.append(c)

for i in a:
    s = ["%6d" % x for x in i]
    print(' '.join(s))

b = [1, 1, 2, 3, 5, 8, 13, 21]
a = []
t = a
for i in b:
    t.append(i)
    c = []
    t.append(c)
    print(t)
    t = c
print(a)


# import from for in if elif else
# def return
# 关键字keyword，拥有特殊含义

# define 定义一个函数，
"""
def 函数名(参数1, 参数2, ...):
    一些代码
"""
def f(x):
    return x * x

print(f(1), f(3), pow(1, 2), pow(3, 2))

# 数学上叫做分段函数
def g(x):
    if x > 0:
        return -x
    else:
        return x ** 2
from matplotlib import pyplot
import math
X = [(math.pi * i / 25) for i in range(1, 80)]
Y = [math.sin(i) for i in X]
pyplot.plot(X, Y)
pyplot.axis('equal')
pyplot.show()

def fb(n):
    if n <= 2:
        return 1
    a, b = 1, 1

# 最大公约数
def gcd(a, b):
    return -1 # 返回一个值


# 最小公倍数
def lcm(a, b):
    return -1

