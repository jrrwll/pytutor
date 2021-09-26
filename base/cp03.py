#!/usr/bin/env python3
# coding=utf-8

"""
内存复用
"""

# 斐波拉契数列
# a  a(n-2)
# b  a(n-1)
# c  a(n)
# a(n) = a(n-1) + a(n-2)
# a(n+1) = a(n) + a(n-1)
a = 1
b = 1
print(1)
print(1)
for i in range(3, 21):
    c = a + b
    print(i, a, b, c)
    a = b
    b = c

a, b = 3, 5
print(a, b) # 3 5
# TODO
print(a, b) # 8 3 5

a, b, c = 3, 5, 8
print(a, b, c) # 3 5 8
# TODO
print(a, b, c) # 8 3 5

