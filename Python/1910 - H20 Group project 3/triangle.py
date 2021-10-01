import numpy as np
import matplotlib.pyplot as plt


# 1a)

def triangle_corner(c0, c1):
    """
    Creates the third and last corner of a triangle

    Parameters
    ----------
    Given corners
    c0 = (0, 0) :   tuple
                    first corner
    c1 = (1, 0) :   tuple
                    second corner

    Returns
    ---------
    Array
        with the three corners c0, c1 and c2
    """

    if len(c0) != 2 and len(c1) != 2:
        print("Punkt ugyldige")
        return 0

    c2 = ((abs(c1[0] - c0[0])) / 2, np.sin(np.pi / 3))
    return np.array([c0, c1, c2])


def plot(c):
    """
    Plotting the corners
    :rtype: Plot

    Parameters
    ---------
    c : array or list
        the three corners c0, c1 and c2
    """
    plt.scatter(*zip(*c), color='blue', marker='.')
    plt.axis('equal')
    plt.axis('off')


def starting_point():
    """
    Generating random, scaled starting points, and returning a list of them
    """
    weights = np.random.random(size=len(corners))
    scaled_weights = weights / sum(weights)
    starting_point = []
    starting_point += [sum([scaled_weights[j] * corners[j] for j in range(len(corners))])]

    return starting_point


def points_within(N):
    """
    Adding points within the triangle using the given algorithm

    Parameter
    ---------
    N : int
        number of points

    Returns
    -------
    points : list
        a list of N points within the triangle
    """
    points = []
    points += starting_point()

    for i in range(1, N + 6):
        j = np.random.randint(3)
        points += [(points[i - 1] + corners[j]) / 2]
    return points[5:]


def adding_color(N):
    """
    Adding points within the triangle,
    and attributing a color according to its starting point

    Parameter
    ---------
    N : int
        number of points

    Returns
    -------
    points : list
        a list of N points within the triangle
    colors : list
        a list of N colors attributed to each point
    """
    points = []
    points += starting_point()

    colors = []

    for i in range(1, N + 5):
        j = np.random.randint(3)
        colors += [j]
        points += [(points[i - 1] + corners[j]) / 2]
    return points[5:], colors[4:]


def plot_colors(N):
    """
    Plots the points and their color

    Parameter
    ---------
    N : int
        the number of points
    """
    R = []
    G = []
    B = []
    points, colors = adding_color(N)

    for i in range(len(points)):
        if colors[i] == 0:
            R += [points[i]]

        elif colors[i] == 1:
            G += [points[i]]

        else:
            B += [points[i]]

    plt.scatter(*zip(*R), s=0.1, c='red', marker='.')
    plt.scatter(*zip(*G), s=0.1, c='green', marker='.')
    plt.scatter(*zip(*B), s=0.1, c='blue', marker='.')

    plt.axis('equal')
    plt.axis('off')


def alternative_colors(N, corners):
    """
    Computs the individual RGB color value for each point, and plots it

    Parameters
    ----------
    N : int
        the number of points
    corners : array
        the corners of the triangle
    """
    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 1, 0])
    r3 = np.array([0, 0, 1])
    r = np.array([r1, r2, r3])

    colors = np.zeros((N, 3))
    colors[0] = np.array([0, 0, 0])
    points = np.zeros((N, 2))
    for i in range(1, N - 1):
        j = np.random.randint(3)
        colors[i + 1] = (colors[i] + r[j]) / 2
        points[i + 1] = (points[i] + corners[j]) / 2

    plt.scatter(*zip(*points), c=colors, s=0.2, marker='.')
    plt.axis('equal')
    plt.axis('off')


if __name__ == '__main__':

    N = 10000

    # 1a
    """
    Given corners
    c0 = (0, 0)
    c1 = (1, 0)
    """
    c0 = (0, 0)
    c1 = (1, 0)
    corners = triangle_corner(c0, c1)
    plot(corners)
    plt.show()

    # 1b
    for i in range(1000):
        plot(starting_point())
    plt.show()

    # 1d
    plot(points_within(N))
    plt.show()

    # 1e
    plot_colors(N)
    plt.show()

    # 1f
    alternative_colors(N, corners)
    plt.show()