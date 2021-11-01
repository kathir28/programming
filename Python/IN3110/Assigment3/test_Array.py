from Array import *


def test_print():
    #checks if print output is correct
    test_a = Array((4,), 2, 3, 1, 0)
    assert str(test_a) == '2   3   1   0   '


def test_add_floats():
    #adds an array with an float and checks output
    test_a = Array((4,), 2, 3, 1, 0)
    test_b = test_a + 1.2
    sol = Array((4,), 3.2, 4.2, 2.2, 1.2)
    assert str(test_b) == str(sol)


def test_add_ints():
    # adds an array with an int and checks output
    test_a = Array((4,), 2, 3, 1, 0)
    test_b = test_a + 1
    sol = Array((4,), 3, 4, 2, 1)
    assert str(test_b) == str(sol)


def test_add_array():
    # adds an array with an another array and checks output
    test_a = Array((4,), 2, 3, 1, 0)
    test_b = Array((4,), 2, 3, 1, 0)
    sol = Array((4,), 4, 6, 2, 0)
    test = test_a + test_b
    assert str(sol) == str(test)






def test_sub_array():
    # substracts  an array with an array and checks output
    test_a = Array((4,), 2, 3, 1, 0)
    test_b = Array((4,), 4, 8, 9, 1)
    test = test_a - test_b
    sol = Array((4,), -2, -5, -8, - 1)
    assert str(test) == str(sol)



def test_mul_array():
    # multiplies  an array with an array and checks output
    test_a = Array((4,), 2, 3, 1, 0)
    test_b = Array((4,), 4, 8, 9, 1)
    test = test_a * test_b
    sol = Array((4,), 8, 24, 9, 0)
    assert str(test) == str(sol)

def test_mul_num():
    # substracts  an int with an array and checks output
    test_a = Array((4,), 2, 3, 1, 0)
    test = 2*test_a
    sol = Array((4,), 4, 6, 2, 0)
    assert str(test) == str(sol)

def test_compare():
    # compares size  an array with another array and checks output
    test_a = Array((4,), 4, 3, 1, 0)
    test_b = Array((4,), 4, 7, 10, 1)
    assert  test_a == test_b

def test_compare_unequal():
    #checks if it returns false when size is not equal
    test_a = Array((4,), 4, 3, 1, 0)
    test_b = Array((5,), 4, 7, 10, 1, 2)
    test = test_a == test_b
    assert  test == False

def test_isequal():
    #checks if two arrays are equal
    test_a = Array((4,), 4, 3, 1, 0)
    test_b = Array((4,), 4, 3, 1, 0)
    assert  test_a.is_equal(test_b) == True


def test_isequal_num():
    #checks if it finds the number for each element in the array
    test_a = Array((4,), 4.2, 3, 1, 0)
    test_n = 4.2
    sol = Array((4,), True, False, False , False)
    assert  str(test_a.is_equal(test_n)) == str(sol)

def test_min():
    #tests minimum
    test_a = Array((4,), 4.2, 3, -100, 0)
    assert test_a.min_element() == -100

    test_b = Array((4,), 4.2, 1, 6, 50)
    assert test_b.min_element() == 1

def test_add_int_2d():
    #checks if two dimensional addition with arrays works
    test_a = Array((4,2), 2, 3, 1, 0,1,3,4,5)
    test_b = Array((4,2), 1, 3, 6, 0,1,3,4,0)
    test = test_a + test_b
    sol = Array((4,2), 3 , 6, 7 , 0 , 2 , 6, 8, 5)
    assert  str(test) == str(sol)

def test_sub_int_2d():
    # checks if two dimensional subbtraction with arrays works
    test_a = Array((4,2), 5, 8, 9, 10,9 , 6,8,10)
    test_b = Array((4,2), 1, 3, 6, 0,1,3,4,0)
    test = test_a - test_b
    sol = Array((4,2), 4 , 5, 3 , 10 , 8 , 3, 4, 10)
    assert  str(test) == str(sol)

def test_eq_2d():
    # checks if two dimensional array size match works
    test_a = Array((4, 2), 5, 8, 9, 10, 9, 6, 8, 10)
    test_b = Array((4, 2), 1, 3, 6, 0, 1, 3, 4, 0)
    assert test_a == test_b

def test_isequal_2d():
    #checks if it returns false when arrays are not identical
    test_a = Array((4, 2), 5, 8, 9, 10, 9, 6, 8, 10)
    test_b = Array((4, 2), 1, 3, 6, 0, 1, 3, 4, 0)
    test = test_a.is_equal(test_b)
    assert test == False

    # checks if it returns true when arrays are identical
    test_a = Array((4, 2), 5, 8, 9, 10, 9, 6, 8, 10)
    test_b = Array((4, 2), 5, 8, 9, 10, 9, 6, 8, 10)
    test = test_a.is_equal(test_b)
    assert test == True