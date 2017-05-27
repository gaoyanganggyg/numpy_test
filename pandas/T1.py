import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def t1():
    a = pd.Series([1, 3, 5, np.nan, 10])
    print a


def t2():
    a = pd.date_range('20130101', periods=6)
    print a

    d = pd.DataFrame(np.random.randn(6, 4), index=a, columns=list('ABCD'))
    print d.head()
    print d
    print d.tail(2)
    print d.index
    print d.columns
    print d.values
    print d.T
    print d.describe()

    print d.sort_index(axis=1, ascending=False)
    print d
    print d.sort()


def t3():
    a = pd.date_range('20130101', periods=6)

    d = pd.DataFrame(np.random.randn(6, 4), index=a, columns=list('ABCD'))
    print d['B']
    print d[1:3]
    print d['20130103':]


def t4():
    a = pd.Series(np.random.randn(1000), index=pd.date_range('25/5/2017', periods=1000))
    a = a.cumsum()
    a.plot()


if __name__ == '__main__':
    # t3()
    t4()