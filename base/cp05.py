#!/usr/bin/env python3
# coding=utf-8

"""
猜数字
"""

def main(value, expect):
    a = 0
    c = 0
    for i in range(0, 4):
        if value[i] == expect[i]:
            a = a + 1
    for i in range(0, 4):
        if value[i] in expect:
            c = c + 1
    b = c - a
    return str(a) + 'A' + str(b) + 'B'


if __name__ == '__main__':
    answer = '7956'
    print(main('7956', answer))


import random
persons = [
    '冬',
    '柳',
    '风',
    '月',
    '元',
    '珠',
    '鼠',
    '南',
    '襄',
    '范',
]

for i in range(0, 6):
    idx = random.randint(0, len(persons))
    person = persons[idx]
    print(person)
    persons.remove(person)

