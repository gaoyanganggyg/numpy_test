import numpy as np


def t1():
    a = np.arange(10, dtype=np.float)
    print a


def t2():
    a = np.linspace(0, 20, 13)
    print a


def t3():
    a = np.logspace(10, 20, base=2, dtype=int)
    print a

if __name__ == '__main__':
    t1()
    t2()
    t3()