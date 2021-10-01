#creating a test for checking exp_decay
#check call func
 
import unittest 
from exp_decay import ExponentialDecay

class test_exp_decay(unittest.TestCase):  
    def test_der(self): 

        X = ExponentialDecay(0.4) 
        S = X(3.2, 1) 

        self.assertAlmostEqual(S, -1.28)


""" 
Terminal > python3 -m unittest test_exp_decay.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK 
""" 