from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt



class ExponentialDecay:
    """
    Creating a class for solving RHS of ODEs as equations of motion for a pendulum.
    """
    def __init__(self, a):
        """
        Class constructor.
        """

        self.a = a

    def __call__(self, u, t):
        """
        Class call method returning derivative.
        """

        return -self.a * u
    

    def solve(self, u0, T, dt):
        """
        Solve method for solving ODE with given initial conditions and an interval.
        """

        sol = solve_ivp(self.__call__, (T, 0), [u0, ], t_eval=np.arange(0, T, dt))
        return sol.t, sol.y[0]



if __name__ == '__main__':
    decay_model = ExponentialDecay(0.4)
    t, u = decay_model.solve(1, 1000, 50)
    plt.plot(t, u)
    plt.show()
