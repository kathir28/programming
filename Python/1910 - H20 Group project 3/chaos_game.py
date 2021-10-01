import numpy as np
import matplotlib.pyplot as plt


class ChaosGame:
    def __init__(self, n, r=0.5):
        """
        Creates and plotts fractals of n-gones
        :rtype: object
        """
        if not isinstance(n, int):
            raise TypeError("N is not an int")
        if not isinstance(r, float):
            raise TypeError("R is not a float ")
        if n >= 3 and (0 < r < 1):
            self.n = n
            self.r = r
            self.corners = self._generate_ngon()
        else:
            raise ValueError("""Either n,r or n and r are not within legal bounds. 
            N must be greather or equal to three and r must be in the interval (0,1)""")

    def _generate_ngon(self):
        """
        Generates the corners of the n-gon

        Parameters
        ----------
        Take no parameters

        Returns
        -------
        corners : array
            corners of the n-gon
        """
        c = np.linspace(0, 2 * np.pi, self.n + 1)
        corners = []
        for z in c[:-1]:
            corners.append([np.sin(z), np.cos(z)])
        corners = np.asarray(corners)
        return corners

    def _starting_point(self):
        """
        Creates a random starting point within the n-gon

        Parameters
        ----------
        Take no parameters

        Returns
        -------
        starting_point : list
            point within the n-gon
        """
        corners = self.corners
        n = self.n
        starting_point = []
        weights = np.random.random(n)
        scaled_weights = weights / sum(weights)
        starting_point += [scaled_weights[j] * corners[j] for j in range(len(corners))]
        return sum(starting_point)

    def plot_ngon(self):
        """
        Plots the corners of the created n-gon
        """
        plt.scatter(*zip(*self.corners), marker=".")
        plt.axis('equal')
        plt.axis('off')
        plt.show()

    def iterate(self, steps, discard=5):
        """
        Picks a random corner in the n-gon and then computes the next point

        Parameters
        ----------
        steps : int
            number of points
        discard : int
            number of discated points
        """
        self.x = np.zeros((steps + discard, 2))
        self.x[0] = self._starting_point()

        for i in range(steps + discard - 1):
            k = np.random.randint(self.n)
            self.x[i + 1] = self.r * (self.x[i] + (1 - self.r) * self.corners[k])
        self.x = self.x[discard:]

    """
    @property
    def gradient_color():
        C[i+1] = (C[i] + j[i+1]) / 2
    """

    def plot(self, color=False, cmap="jet"):
        """
        Plots the generated n-gon

        Parameters
        ----------
        color : bol
        cmap : string
        """
        if color:
            cmap = self.gradient_color()

        else:
            cmap = "Black"

            plt.scatter(*zip(*self.x), c=cmap, s=0.2, marker='.')
            plt.axis('equal')
            plt.axis('off')

    def show(self, color=False, cmap="jet"):
        """
        Calles the plot method and shows the plot
        """
        self.plot()
        plt.show()

    def savepng(self, outfile, color=False, cmap="jet"):
        """
        Saves the plot of the n-gon

        Parameters
        ----------
        outfile : string
            the name of the file
        """
        if "." not in outfile:
            outfile = outfile + ".png"

        elif outfile[-4:] == ".png":
            outfile = outfile

        elif outfile[-4:] != ".png":
            raise TypeError("File type must be .png")

        self.plot()
        plt.savefig(outfile, dpi=300)


if __name__ == '__main__':

    # 2b
    n3 = ChaosGame(3)
    n4 = ChaosGame(4)
    n5 = ChaosGame(5)
    n6 = ChaosGame(6)
    n7 = ChaosGame(7)
    n8 = ChaosGame(8)

    n3.plot_ngon()
    n4.plot_ngon()
    n5.plot_ngon()
    n6.plot_ngon()
    n7.plot_ngon()
    n8.plot_ngon()

    # 2c
    # Test for starting point
    pentagon = []
    for i in range(100000):
        # Måtte litt opp i range for å se at det er et pentagram
        pentagon += [n5._starting_point()]
    plt.scatter(*zip(*pentagon), marker='.', s=0.1)
    plt.axis('equal')
    plt.axis('off')
    plt.show()

    # 2i
    n3 = ChaosGame(3, 1 / 2)
    n4 = ChaosGame(4, 1 / 3)
    n5 = ChaosGame(5, 1 / 3)
    n5_2 = ChaosGame(5, 3 / 8)
    n6 = ChaosGame(6, 1 / 3)

    n3.iterate(10000)
    n4.iterate(10000)
    n5.iterate(10000)
    n5_2.iterate(10000)
    n6.iterate(10000)

    n3.savepng("chaos1.png")
    n4.savepng("chaos2.png")
    n5.savepng("chaos3.png")
    n5_2.savepng("chaos4.png")
    n6.savepng("chaos5.png")