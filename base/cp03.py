#!/usr/bin/env python3
# coding=utf-8

"""
内存引用和集合
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

a = [1, 2, 3, 4, 5]
# a[i] 意思是取a的第i+1个元素
print(a[0], a[1], a[2], a)
# a[i] = b，意思是将b赋值给a的第i+1个元素
a[0] = -1 # 把-1赋值给a的第一个元素
print(a) # -1 2 3 4 5
# TODO
print(a) # 5 4 3 2 -1

# [1, 4, 9, 16, 25, 36, 49, ... n**2]
a = []
for i in range(1, 21):
    # list的方法(函数)，添加一个元素到列表的尾端
    a.append(i ** 2)
print(a)
a.clear()

a = [1, 2, 3]
a.insert(1, -4) # 插入-4到1位
b = a.pop(1) # pop 删除i位并且将其返回(第i+1个元素)
print(a, b)

# // 整除取商，比如 5//2为 2
x = len(a)
y = len(a) // 2
print(y)
# 有y对元素需要交换，其中 a[i] 需要和 a[x-i-1] 交换
# i的取值为从0到y-1
# a[0] --- a[x-1]
# a[1] --- a[x-2]
# a[i] --- a[x-i-1]
for i in range(0, y):
    # 将a[i] 和 a[x-i-1] 交换
    m=a[i]
    a[i]=a[x-i-1]
    a[x-i-1]=m
    print(a)
