#!-*-coding:utf-8-*-
import numpy as np


def t1():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print  '原始数组是：'
    print a
    print  '\n'
    print  '修改后的数组是：'
    for x in np.nditer(a):
        print x,


def t2():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print  '原始数组是：'
    print a
    print  '\n'
    print  '原始数组的转置是：'
    b = a.T
    print b
    print  '\n'
    print  '修改后的数组是：'
    for x in np.nditer(b):
        print x,


def t3():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print  '原始数组是：'
    print a
    print  '\n'
    print  '原始数组的转置是：'
    b = a.T
    print b
    print  '\n'
    print  '以 C 风格顺序排序：'
    c = b.copy(order='C')
    print c
    for x in np.nditer(c):
        print x,
    print  '\n'
    print  '以 F 风格顺序排序：'
    c = b.copy(order='F')
    print c
    for x in np.nditer(c):
        print x,


def t4():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print  '原始数组是：'
    print a
    print  '\n'
    print  '以 C 风格顺序排序：'
    for x in np.nditer(a, order='C'):
        print x,
    print  '\n'
    print  '以 F 风格顺序排序：'
    for x in np.nditer(a, order='F'):
        print x,


def t5():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print  '原始数组是：'
    print a
    print  '\n'
    for x in np.nditer(a, op_flags=['readwrite']):
        x[...] = 2 * x
    print  '修改后的数组是：'
    print a


def t6():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print  '原始数组是：'
    print a
    print  '\n'
    print  '修改后的数组是：'
    for x in np.nditer(a, flags=['external_loop'], order='F'):
        print x,


def t7():
    a = np.arange(0, 60, 5)
    a = a.reshape(3, 4)
    print  '第一个数组：'
    print a
    print  '\n'
    print  '第二个数组：'
    b = np.array([1, 2, 3, 4], dtype=int)
    print b
    print  '\n'
    print  '修改后的数组是：'
    for x, y in np.nditer([a, b]):
        print  "%d:%d" % (x, y),

if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    # t4()
    # t5()
    # t6()
    t7()