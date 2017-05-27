import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    x = np.arange(0, np.pi*2, step=0.01)
    y = np.cos(x)
    plt.xlim(x.min(), x.max())
    plt.xlabel("X")
    plt.ylim(y.min(), y.max())
    plt.ylabel("Y")
    plt.plot(x, y,)
    plt.show()
    print x