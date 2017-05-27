import numpy as np


def t1():
    a = np.array([1, 3, 5], dtype=np.int, ndmin=3)
    print a


def t2():
    d = np.dtype(np.int32)
    print d


def t3():
    d = np.dtype([('age', np.int8)])
    a = np.array([(10,), (20,), (30,)], dtype=d)
    print a['age']


def t4():
    student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
    a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
    print a['name']


def t5():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print a.shape


def t6():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    a.shape = (3, 2)
    print a


def t7():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = a.reshape(3, 2)
    print b


def t8():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print a.ndim


def t9():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print a.flags

if __name__ == '__main__':
    t1()
    t2()
    t3()
    t4()
    t5()
    t6()
    t7()
    t8()
    t9()
