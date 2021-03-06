import glob
import numpy as np
import seaborn as sbn
from sklearn.linear_model import RANSACRegressor, LinearRegression
from matplotlib import pyplot as plt


def display_results(dir_name, title):
    names = glob.glob('out/%s/*.txt' % dir_name)
    for n in names:
        clean_name = n.split('/')[-1].split('.')[0]

        x = np.arange(0, 256)
        plt.plot(x, (0.3 * x + 5), label='baseline', lw=7)
        x, y = np.loadtxt(n)
        y = np.square(y)

        plt.plot(x, y, ':', label=clean_name)

        ransac = RANSACRegressor(LinearRegression())
        x = x.reshape(-1, 1)
        print(x.shape)
        # y.reshape(-1, 1)
        print(x, y)
        ransac.fit(x, y)

        y_ransac = ransac.predict(x)
        x = x.reshape(-1)
        plt.plot(x, y_ransac)
        #
        plt.legend()
        plt.show()


display_results('signal_dependent', 'Signal dependent noise')
