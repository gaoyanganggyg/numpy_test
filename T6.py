#!-*-coding:utf-8-*-
import numpy as np


def t1():
    a = np.arange(10, 30)
    s = slice(10, 23, 3)
    print a[s]
    print a[10:23:1]


def t2():
    # 最开始的数组
    import numpy as np
    a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
    print  '我们的数组是：'
    print a
    print  '\n'
    # 这会返回第二列元素的数组：
    print  '第二列的元素是：'
    print a[..., 1]
    print  '\n'
    # 现在我们从第二行切片所有元素：
    print  '第二行的元素是：'
    print a[1, ...]
    print  '\n'
    # 现在我们从第二列向后切片所有元素：
    print  '第二列及其剩余元素是：'
    print a[..., 1:]

    print a[1:, ...]


def t3():
    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print  '我们的数组是：'
    print x
    print  '\n'
    rows = np.array([[0, 0], [3, 3]])
    cols = np.array([[0, 2], [0, 2]])
    print rows
    print cols
    y = x[rows, cols]
    print  '这个数组的每个角处的元素是：'
    print y


def t4():
    x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
    print  '我们的数组是：'
    print x
    print  '\n'
    # 现在我们会打印出大于 5 的元素
    print  '大于 5 的元素是：'
    print x[x > 5]


def t5():
    a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
    print a[~np.isnan(a)]


if __name__ == '__main__':
    t1()
    t2()
    t3()
    t4()
    t5()