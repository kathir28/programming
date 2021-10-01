from pendulum import Pendulum 
import numpy as np
import unittest  


class test_pendulum(unittest.TestCase): 

    def test_rest(self):
        initialv = Pendulum()
        initialv.solve((0, 0), 30, 1000, "rad")
        assert np.isclose(np.zeros(len(initialv.theta)), initialv.theta, rtol=0.001).any()
        assert np.isclose(np.zeros(len(initialv.w)), initialv.w, rtol=0.001).any()

    def test_sol(self):

        y = [np.pi/6, 0.15]
        A = Pendulum(2.7, 1)
        B = A(1, y)

        np.testing.assert_almost_equal(B[1], -1.816666666)
        np.testing.assert_almost_equal(B[0], 0.15)

    def test_car(self):
        Pendel = Pendulum()
        Pendel.solve((1, 4), 10, 100)
        x = Pendel.x
        y = Pendel.y
        r = x**2 + y**2
        assert np.isclose(r, Pendel.L, rtol=0.3).any() 


    def test_time(self):
        initialv= Pendulum()
        initialv.solve((0,0), 30, 1000, "rad")
        np.array_equal(np.linspace(0,30,1000), initialv.t)


        
    def test_prop(self):
        initialV = Pendulum()
        initialV.solve((0, 0), 30, 1000, "rad")
        np.testing.assert_equal(initialV.solve.has_been_called, True) #retunerer feil
        #np.testing.assert_equal(self.theta.has_been_called, False)
        #np.testing.assert_equal(self.omega.has_been_called, False)


        




"""

def test_pendulum_properties():

    y0 = (0,0)
    T = 10
    expected = np.zeros(T)
    pend1= pendulum()
    solve = pend1.solve(y0,T,1)
    computed = pend1.theta
    
"""
    
 


    

  