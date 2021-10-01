import numpy as np
import matplotlib.pyplot as plt

class AffineTransform:
    def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def __call__(self, p0):
        x, y = p0
        x0 = self.a * x + self.b * y + self.e
        y0 = self.c * y + self.d * y + self.f
        return x0, y0

if __name__ == "__main__":
    f1 = AffineTransform(0, 0, 0, 0.16, 0, 0)
    f2 = AffineTransform(0.85, 0.04, -0.04, 0.85, 0, 1.60)
    f3 = AffineTransform(0.20, -0.26, 0.23, 0.22, 0, 1.60)
    f4 = AffineTransform(-0.15, 0.28, 0.26, 0.24, 0, 0.44)
    functions = [f1, f2, f3, f4]
    probabilities = [0.01, 0.85, 0.07, 0.07]

    def non_uniform_drawing(functions):
        if sum(probabilities) == 1:
            p_cumulative = np.cumsum(probabilities)
            r = np.random.random()
            for j, p in enumerate(p_cumulative):
                if r < p:
                    return functions[j]

        else:
            raise ValueError("Not valid probabilities! The sum must be equal to 1")


    def iterating(N):
        p0 = ([0,0])
        points = []
        for _ in range(N):
            function = non_uniform_drawing(functions)
            new_point = function(p0)
            points.append(new_point)
            p0 = new_point
        return points

    def plotting(N=50000):
        plt.scatter(*zip(*iterating(N)),s=0.1,color ="forestgreen", marker = '.')
        plt.axis('equal')
        plt.axis('off')
        plt.savefig('barnsley_fern.png')
        plt.show()

    plotting()
    plt.show()
