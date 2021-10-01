import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.animation as animation

g = 9.81


class DoublePendulum:
    """
    Creating class for physical system of a double pendulum.
    """
    def __init__(self, M1=1, L1=1, M2=1, L2=1):
        """ 
        Class constructor.
        """

        if not isinstance(L1, int):
            if not isinstance(L1, float):
                raise ValueError('Verdi ikke float eller int')
        if not isinstance(M1, int):
            if not isinstance(M1, float):
                raise ValueError('Verdi ikke float eller int')
        if not isinstance(L2, int):
            if not isinstance(L2, float):
                raise ValueError('Verdi ikke float eller int')
        if not isinstance(M2, int):
            if not isinstance(M2, float):
                raise ValueError('Verdi ikke float eller int')

        self.L1 = L1
        self.M1 = M1
        self.L2 = L2
        self.M2 = M2
        self.theta1 = []  
        self.theta2 = []
        self.w1 = []
        self.w2 = []
        self.t = 0
        self.sjekk = False


    def __call__(self, t, y):
        """
        Call method returning derivatives.
        """

        self.theta1 = y[0]
        self.theta2 = y[2]
        self.w1 = y[1]
        self.w2 = y[3] 
        self.dtheta = self.theta2 - self.theta1
        dw1 = (self.M2 * self.L1 * (self.w1**2) * np.sin(self.dtheta) * np.cos(self.dtheta) + self.M2 * g * np.sin(self.theta2) * np.cos(self.dtheta) + self.M2 * self.L2 * (self.w2**2) * np.sin(self.dtheta) - (self.M1 + self.M2) * g * np.sin(self.theta1))/((self.M1 + self.M2) * self.L1 - self.M2 * self.L1 * np.cos(self.dtheta) ** 2)
        dw2 = (-self.M2 * self.L2 * self.theta2 ** 2 * np.sin(self.dtheta) * np.cos(self.dtheta) + (self.M1 + self.M2) * g * np.sin(self.theta1) * np.cos(self.dtheta) - (self.M1 + self.M2) * self.L1 * (self.w1 ** 2) * np.sin(self.dtheta) - (self.M1 + self.M2) * g * np.sin(self.theta2))/((self.M1 + self.M2) * self.L2 - self.M2 * self.L2 * (np.cos(self.dtheta) ** 2))
        return self.w1, dw1, self.w2, dw2 

    def solve(self, u0, T, dt, angles="rad"):
        """ 
        Solve function for ODEs with given inital values and interval 
        """

        if angles == "rad":
            pass
        elif angles == "deg":
            u0 = np.deg2rad(u0)
        else:
            raise ValueError("Input only accepts rad or deg")
        print(u0)

        sol = solve_ivp(self.__call__, (0, T), u0, t_eval=np.linspace(0, T, dt), method="Radau")
        self.t = sol.t
        self.w1 = sol.y[1]
        self.w2 = sol.y[3]
        self.theta1 = sol.y[0]
        self.theta2 = sol.y[2]
        self.sjekk =True

    def create_animation(self):  
    
        """ 
        Function for creating the animation of the double pendulum  
        """

        # Create empty figure
        fig = plt.figure()
        
        # Configure figure
        plt.axis('equal')
        plt.axis('off')
        plt.axis((-3, 3, -3, 3))
        
        # Make an "empty" plot object to be updated throughout the animation
        self.pendulums, = plt.plot([], [], 'o-', lw=2)
        
        # Call FuncAnimation
        self.animation = animation.FuncAnimation(fig,
                                                 self.next_frame,
                                                 frames=range(len(self.x1)), 
                                                 repeat=None,
                                                 interval=600, 
                                                 blit=True)

    def next_frame(self, i): 
        """ 
        Function for calculating the next frame in the animation of the double pendulum.  
        """

        self.pendulums.set_data((0, self.x1[i], self.x2[i]),
                                (0, self.y1[i], self.y2[i]))
        return self.pendulums, 
    

    def show_animation(self): 
        """ 
        Function for showing the animation.
        """

        plt.show()
    

    def save_animation(self): 
        """  
        Function for saving the animation as a video file.
        """ 

        self.animation.save("example_simulation.mp4", fps=60) 


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
    def theta_1(self):
        """ 
        Property function to access the solutions from outside the object for theta1.
        """
        """
        if hasattr(self, "sol"):
            return self.theta1
        else:
            raise AttributeError
        """
        if self.sjekk:
            return self.theta1
        else:
            raise AttributeError


    @property
    def theta_2(self):
        """
        Property function to access the solutions from outside the object for theta2.
        """
        """    
        if hasattr(self, "sol"):
            return self.theta2
        else:
            raise AttributeError
        """
        if self.sjekk:
            return self.theta2
        else:
            raise AttributeError
    @property
    def omega1(self):
        """ 
        Property function to access the solutions from outside the object for omega1.
        """
        """
        if hasattr(self, "sol"):
            return self.w1
        else:
            raise AttributeError
        """
        if self.sjekk:
            return self.w1
        else:
            raise AttributeError
    @property
    def omega2(self):
        """ 
        Property function to access the solutions from outside the object for omega2.
        """
        """
        if hasattr(self, "sol"):
            return self.w2
        else:
            raise AttributeError
        """
        if self.sjekk:
            return self.w2
        else:
            raise AttributeError
    @property
    def x1(self):
        """
        Property function returning cartesian coordinates for x1.
        """

        return self.L1 * np.sin(self.theta1) 

    @property
    def x2(self):
        """
        Property function returning cartesian coordinates for x2.
        """

        return self.x1 + self.L2 * np.sin(self.theta2)

    @property
    def y1(self):
        """
        Property function returning cartesian coordinates for y1.
        """

        return -self.L1 * np.cos(self.theta1)

    @property
    def y2(self):
        """
        Property function returning cartesian coordinates for y2.
        """

        return self.y1 - self.L2 * np.cos(self.theta2)

    @property
    def potential(self):  
        """
        Property function returning potential energy of double pendulum
        """

        P1 = self.M1 * g * (self.y1 + self.L1) 
        P2 = self.M2 * g * (self.y2 + self.L1 + self.L2) 
        tot_p = P1 + P2 
        return tot_p 

    @property 
    def vx1(self): 
        """
        Property function returning cartesian coordinates for velocity for x1.
        """
        return np.gradient(self.x1, self.t)

    @property 
    def vx2(self):  
        """
        Property function returning cartesian coordinates for velocity for x2.
        """
        return np.gradient(self.x2, self.t)

    @property
    def vy1(self):  
        """
        Property function returning cartesian coordinates for velocity for y1.
        """
        return np.gradient(self.y1, self.t)

    @property
    def vy2(self): 
        """
        Property function returning cartesian coordinates for velocity for y2.
        """
        return np.gradient(self.y2, self.t)

    @property
    def kinetic(self):  
        """
        Property function returning kinetic energy of double pendulum.
        """

        K1 = 0.5 * self.M1 * ((self.vx1 ** 2) + (self.vy1 ** 2))
        K2 = 0.5 * self.M2 * ((self.vx2 ** 2) + (self.vy2 ** 2))
        tot_k = K1 + K2 
        return tot_k 

    @property
    def Total(self):
        """
        Property function returning total energy of double pendulum.
        """

        return self.kinetic + self.potential
    
    @property
    def to_cartesian(self): 
        """
        All in one creating cartesian coordinates for x1, x2, y1, y2
        """
        return self.L1 * np.sin(self.theta1), self.x1 + self.L2 * np.sin(self.theta2), -self.L1 * np.cos(self.theta1), self.y1 - self.L2 * np.cos(self.theta2)


    def chaotic_pendulum(self): 
        """
        Function for creating a unpredictable chaotic pendulum
        """

        y0 = [(np.pi / 6, 0.15, np.pi / 6, 0.15), (np.pi / 3, 0.1, np.pi / 3, 0.1), (np.pi, 0.05, np.pi, 0.05)]
        n = 0
        for init in y0:
            dp = DoublePendulum()
            dp.solve(init, 10, 100)
            x1, y1, x2, y2 = dp.to_cartesian
            plt.plot(x1, y1, label=f"(x1, y1) list index {n}")
            plt.plot(x2, y2, label=f"(x2, y2) list index {n}")
            plt.legend()
            plt.xlabel("t")
            plt.ylabel("y")
            n += 1
        plt.savefig("chaotic_pendulum.png")


if __name__ == '__main__':
    
    Pendel = DoublePendulum()
    Pendel.solve((np.pi/6, 0.15, np.pi/6, 0.15), 10, 1000)
    x1 = Pendel.x1
    y1 = Pendel.y1
    x2 = Pendel.x2 
    y2 = Pendel.y2
    """
    plt.plot(x1, y1, label="x1") 
    plt.plot(x2, y2, label="x2")
    plt.legend(loc="best")
    plt.show()
    """
    plt.plot(Pendel.t, Pendel.kinetic, label="Kinetic") 
    plt.plot(Pendel.t, Pendel.potential, label="Potential") 
    plt.plot(Pendel.t, Pendel.Total, label="Total E")
    plt.legend(loc="best")
    plt.show()

    """
    plt.plot(Pendel.t, Pendel.theta1) 
    plt.show()
    plt.plot(Pendel.t, Pendel.theta)
    plt.plot(Pendel.t, Pendel.w)
    plt.show()
    plt.plot(Pendel.t, Pendel.kinetic)
    plt.plot(Pendel.t, Pendel.Total)
    plt.show()
    """ 
    Pendel = DoublePendulum()
    Pendel.solve((np.pi/6, 0.15, np.pi/6, 0.15), 10, 1000)
    fig = plt.figure() 
    Pendel.create_animation()
    for i in range(len(Pendel.t)): 
        Pendel.next_frame(i) 
    Pendel.animation.save('example_simulation.mp4')
    Pendel.chaotic_pendulum()
    
