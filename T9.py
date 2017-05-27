#!-*-coding:utf-8-*-
import numpy as np


def t1():
    a = np.arange(8).reshape(2, 4)
    print '原始数组：'
    print a
    print '\n'

    print '调用 flat 函数之后：'
    # 返回展开数组中的下标的对应元素
    print a.flat[5]


def t2():
    a = np.arange(8).reshape(2, 4)

    print '原数组：'
    print a
    print '\n'
    # default is column-major

    print '展开的数组：'
    print a.flatten()
    print '\n'

    print '以 F 风格顺序展开的数组：'
    print a.flatten(order='F')


def t3():
    a = np.arange(8).reshape(2, 4)

    print '原数组：'
    print a
    print '\n'

    print '调用 ravel 函数之后：'
    print a.ravel()
    print '\n'

    print '以 F 风格顺序调用 ravel 函数之后：'
    print a.ravel(order='F')


def t4():
    a = np.arange(12).reshape(3, 4)

    print '原数组：'
    print a
    print '\n'

    print '转置数组：'
    print np.transpose(a)

    print a.T


def t5():
    a = np.arange(8).reshape(2, 2, 2)

    print '原数组：'
    print a
    print '\n'
    # 将轴 2 滚动到轴 0（宽度到深度）

    print '调用 rollaxis 函数：'
    print np.rollaxis(a, 2)
    # 将轴 0 滚动到轴 1：（宽度到高度）
    print '\n'

    print '调用 rollaxis 函数：'
    print np.rollaxis(a, 2, 1)



def t6():
    x = np.array([[1], [2], [3]])
    y = np.array([4, 5, 6])

    # 对 y 广播 x
    b = np.broadcast(x, y)
    # 它拥有 iterator 属性，基于自身组件的迭代器元组

    print '对 y 广播 x：'
    r, c = b.iters
    print r.next(), c.next()
    print r.next(), c.next()
    print '\n'
    # shape 属性返回广播对象的形状

    print '广播对象的形状：'
    print b.shape
    print '\n'
    # 手动使用 broadcast 将 x 与 y 相加
    b = np.broadcast(x, y)
    c = np.empty(b.shape)

    print '手动使用 broadcast 将 x 与 y 相加：'
    print c.shape
    print '\n'
    c.flat = [u + v for (u, v) in b]

    print '调用 flat 函数：'
    print c
    print '\n'
    # 获得了和 NumPy 内建的广播支持相同的结果

    print 'x 与 y 的和：'
    print x + y


def t7():
    x = np.arange(9).reshape(1, 3, 3)

    print '数组 x：'
    print x
    print '\n'
    y = np.squeeze(x)

    print '数组 y：'
    print y
    print '\n'

    print '数组 x 和 y 的形状：'
    print x.shape, y.shape

if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    # t4()
    # t5()
    # t6()
    t7()