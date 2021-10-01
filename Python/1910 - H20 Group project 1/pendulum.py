import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

g = 9.81

class Pendulum:
    """
    Creating a class representing the physical system for our pendulum.
    """
    def __init__(self, L=1, M=1):
        """ 
        Class constructor.
        """

        if not isinstance(L, int):
            if not isinstance(L, float):
                raise ValueError('Verdi ikke float eller int')
        if not isinstance(M, int):
            if not isinstance(M, float):
                raise ValueError('Verdi ikke float eller int')

        self.L = L
        self.M = M
        self.theta = []
        self.w = []
        self.t = 0
        self.sjekk = False

    def __call__(self, t, y): 
        """ 
        Class call method returning derivative.
        """ 

        self.theta = y[0]
        self.w = y[1]
        dw = -g / self.L * np.sin(self.theta)
        return self.w, dw

    def solve(self, u0, T, dt, angles="rad"): 
        """
        Solve function for ODE with given initial conditions and an interval. 
        """ 

        if angles == "rad":
            pass
        elif angles == "deg":
            u0 = np.deg2rad(u0)
        else:
            raise ValueError("Input only accepts rad or deg")
        print(u0)

        sol = solve_ivp(self.__call__, (0, T), u0, t_eval=np.linspace(0, T, dt))
        self.t = sol.t
        self.w = sol.y[1]
        self.theta = sol.y[0]
        self.sjekk = True

    @property
    def t_(self):
        """ 
        Property function to access the solutions from outside the object for t.
        """

        """
        Tried using Hasattr func, failed always
        if hasattr(self, "sol"):
            return self.t
        else:
            raise AttributeError
        """
        if self.sjekk:
            return self.t
        else:
            raise AttributeError
    
    @property
    def theta_(self):
        """
        Property function to access the solutions from outside the object for theta.
        """ 
        """
        if hasattr(self, "sol"):
            return self.theta
        else:
            raise AttributeError
        """
        if self.sjekk:
            return self.theta
        else:
            raise AttributeError


    @property
    def omega(self):
        """ 
        Property funciton to access the solutions from outside the object for omega.
        """ 
        """
        if hasattr(self, "sol"):
            return self.w
        else:
            raise AttributeError 
        """
        if self.sjekk:
            return self.w
        else:
            raise AttributeError


    @property
    def x(self):
        """
        Property function returning cartesian coordinates for x.
        """ 

        return self.L * np.sin(self.theta) 


    @property
    def y(self):
        """ 
        Property function returning carsian coordinates for y.
        """ 

        return -self.L * np.cos(self.theta) 


    @property
    def potential(self):  
        """
        Property function returning potential energy of the pendulum.
        """ 

        return self.M*g*(self.y + self.L)


    @property
    def vx(self): 
        """
        Property function returning cartesian coordinates for velocity for x.
        """ 

        return np.gradient(self.x, self.t) 


    @property
    def vy(self): 
        """
        Property function returning cartesian coordinates for velocity for y.
        """ 

        return np.gradient(self.y, self.t)

    @property
    def kinetic(self): 
        """
        Property function returning kinetic energy of the pendulum.
        """ 

        return 0.5*self.M*(self.vx**2 + self.vy**2)


    @property
    def Total(self):
        """
        Property function returning the total energy of pendulum.
        """ 

        return self.kinetic + self.potential


class DampenedPendulum(Pendulum):
    """
    Creating a class for a dampened pendulum.
    """
    def __init__(self, L, M=1, b=2):
        """
        Class constructor.
        """ 

        Pendulum.__init__(self, L,M)
        self.b = b


    def __call__(self, t, y):
        """
        Call method returning derivatives. 
        """ 

        dtheta = y[1]
        w = y[1]
        omega = -(g/self.L) *np.sin(y[0]) - (self.b / self.M) * w
        return dtheta, omega
    

if __name__ == '__main__':
    Pendel = DampenedPendulum(1,10,1)
    Pendel.solve((np.pi/2, 0), 20, 1000)
    #plt.plot(Pendel.t, Pendel.damped)
    #plt.show()
    x = Pendel.x
    y = Pendel.y
    #plt.plot(x ,y)
    #plt.show()
    plt.plot(Pendel.t, Pendel.theta)
    plt.plot(Pendel.t, Pendel.w)
    plt.show()
    plt.plot(Pendel.t, Pendel.kinetic)
    plt.plot(Pendel.t, Pendel.Total)
    plt.show()

    
