import numpy as np


def t1():
    a = np.empty([3, 2], dtype=int)
    print a


def t2():
    a = np.zeros(3, dtype=int, order='F')
    print a


def t3():
    a = np.ones([3, 3])
    print a


if __name__ == '__main__':
    t1()
    t2()
    t3()