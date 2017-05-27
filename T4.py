import numpy as np


def t1():
    x = [1, 2, 3]
    a = np.asarray(x)
    print a


def t2():
    s = "Hello World"
    a = np.frombuffer(s, dtype='S1')
    print a


def t3():
    l = range(10)
    a = np.fromiter(l, dtype=np.int)
    print a


if __name__ == '__main__':
    t1()
    t2()
    t3()
