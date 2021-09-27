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


# 最大公约数
def gcd(a, b):
    return -1


# 最小公倍数
def lcm(a, b):
    return -1

