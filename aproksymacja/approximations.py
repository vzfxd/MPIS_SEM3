from random import random
import matplotlib.pyplot as plt
import numpy as np

from settings import DATA_SET


class Approximation():

    def __init__(self, type_approx, a, b, m, fx, real_value):
        self.type_approx = type_approx
        self.a = a
        self.b = b
        self.m = m
        self.fx = fx
        self.real_value = real_value

    def value_approximation(self, j):
        points = 0
        for i in range(j):
            x = self.a + (self.b - self.a) * random()
            y = self.m * random()
            if (self.type_approx == 'integral' and y <= self.fx(x)):
                points += 1
            elif (self.type_approx == 'circle' and self.fx(x, y)):
                points += 1
        return (points / j) * (self.b - self.a) * self.m

    def plot(self):
        for n in range(50, 5000, 50):
            points_approx = np.array([])
            x_axis = np.array([n for x in range(50)])
            for k in range(50):
                points_approx = np.append(points_approx, self.value_approximation(n))
            avg = np.mean(points_approx)
            plt.scatter(x=x_axis, y=points_approx, s=0.5, c='blue')
            plt.scatter(x=n, y=avg, s=20, c='green')
        plt.plot(np.array([50, 5000]), np.array([self.real_value, self.real_value]), 'r-')
        plt.show()


for obj in DATA_SET:
    approximation = Approximation(obj['type'], obj['data']['a'], obj['data']['b'],
                                  obj['data']['M'], obj['data']['formula'], obj['data']['real_value'])
    approximation.plot()
