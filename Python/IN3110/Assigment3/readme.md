# Readme Assigment 3

Please make sure you have python3 istalled,. You can install this via choco package manager, see install instuctions here: https://chocolatey.org/install

Install python3 by using shell and entring : choco install python

After that you need to make sure you have pytest installed. 

Install instructions :  Go into shell and enter: pip install pytest


## Array Class

I have implemented an array class with some methoeds to resemble numpy functionality. The class works with n dimensional arrays  and contains the elements in a list. 

## Methoeds

str: Converts the array into a nice string to print out 

getitem: retrives the element at a given index. Accepts int and touple input

add: adds arrays with ints, floats and same-size arrays

radd : adds ints, floats with arrays

sub: subtracts rrays with ints, floats and same-size arrays

rsub: subtracts ints and floats with arrays 

mul: multiplies arrays with ints, floats and same-size arrays

rmul : multiplies ints, floats with  arrays

eq: checks if two arrays are of the same size

isequal : Checks if two arrays are identical

min_element: returns the smallest element in the array


## Missing functonality
For n dimensional arrays, you cant access a single element with subscript, for example array[n][m]. The program accepts array[(n.m)]

## Run:

To run the pytest file, please enter in shell: pytest "test Array.py"



