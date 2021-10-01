import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from chaos_game import ChaosGame

class Variations:
    """
    Class that produces variations of figures

    Parameters
    ---------
    x,y,u,v : array or list
              contains the coordinates

    """
    def __init__(self, x, y, name):
        """
        initializer
        """
        self.x = x
        self.y = y
        self.name = name
        self._func = getattr(Variations, self.name)

    def transform(self):
        """
        Converts the initial coordinates with one of
        the static methods, and returns the transformed coordinates
        :parameter: x,y from initializer
        :return: u,v : coordinates
        """
        u, v = self._func(self.x, self.y)
        return u, v

    @staticmethod
    def linear(x, y):
        u = x
        v = y
        return u, v

    @staticmethod
    def handkerchief(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        theta = np.arctan2(x, y)
        u = r * np.sin(theta + r)
        v = np.cos(theta - r)
        return u, v

    @staticmethod
    def swirl(x, y):
        r = np.sqrt(x ** 2 + y ** 2)
        u = x * np.sin(r ** 2) - y * np.cos(r ** 2)
        v = x * np.cos(r ** 2) + y * np.sin(r ** 2)
        return u, v

    @staticmethod
    def disc(x, y):
        theta = np.arctan2(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        u = (theta / np.pi) * np.sin(np.pi * r)
        v = (theta / np.pi) * np.cos(np.pi * r)
        return u, v

    @staticmethod
    def hyperbolic(x, y):
        theta = np.arctan2(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        u = np.sin(theta) / r
        v = r * np.cos(theta)
        return u, v

    @staticmethod
    def hearth(x, y):
        theta = np.arctan2(x, y)
        r = np.sqrt(x ** 2 + y ** 2)
        u = r * np.sin(theta * r)
        v = r * -np.cos(theta * r)
        return u, v

if __name__ == '__main__':
    quad = ChaosGame(4, 1 / 3)
    quad.iterate(10000)
    x = quad.x[:, 0]
    y = quad.x[:, 1]
    transformations = ["linear", "handkerchief", "swirl", "disc"]
    variations = [Variations(x, -y, version) for version in transformations]

    for j in enumerate(variations):
        q = j[1]
        u, v = q.transform()
        t = np.arange(10000)
        plt.scatter(u, -v, s=0.2, marker=".", c= t)
        plt.title(transformations[j[0]])
        plt.show()

    """
    grid_values = np.linspace(-1, 1, 200)
    x, y = np.meshgrid(grid_values, grid_values)
    x_values = x.flatten()
    y_values = y.flatten()
    transformations = ["linear", "handkerchief", "swirl", "disc"]
    variations = [Variations(x_values, y_values, version) for version in transformations]
    

    v_hearth  = Variations(x,y, "hearth")
    u,v = v_hearth.transform()
    plt.scatter(u, -v, s=0.2, marker=".")
    plt.show()

    v_disc = Variations(x, y, "disc")
    u, v = v_disc.transform()
    plt.scatter(u, -v, s=0.2, marker=".")
    plt.show()

    v_linear = Variations(x, y, "linear")
    u, v = v_linear.transform()
    plt.scatter(u, -v, s=0.2, marker=".")
    plt.title("Linear")
    plt.show()

    v_handkerchief = Variations(x, y, "handkerchief")
    u, v = v_handkerchief.transform()
    plt.scatter(u, -v, s=0.2, marker=".")
    plt.title("Handkerchief")
    plt.show()

    v_swirl = Variations(x, y, "handkerchief")
    u, v = v_handkerchief.transform()
    plt.scatter(u, -v, s=0.2, marker=".")
    plt.title("swirl")
    plt.show()

    quad = ChaosGame(4, 1 / 3)
    quad.iterate(10000)
    x = quad.x[:,0]
    y = quad.x[:, 1]
    quad_variation = Variations(x, -y, "disc")
    u, v = quad_variation.transform()
    plt.scatter(u, -v, s=0.2, marker=".")
    plt.title("disc")
    plt.show()

    """
