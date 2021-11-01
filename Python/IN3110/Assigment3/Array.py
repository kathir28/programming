class Array:

    def __init__(self, shape, *values):
        """

        Initialize an array of n-dimensionality. Elements can only be of type:
        - int
        - float
        - bool

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        self.shape = shape

        self.shape_rows = shape[0]
        try:
            self.shape_columns = shape[1]
        except IndexError:
            self.shape_columns = 1
        self.length_array = self.shape_columns * self.shape_rows

        if all(isinstance(x, (int, float, bool)) for x in values):
            if all(isinstance(x, int) for x in values) or all(isinstance(x, float) for x in values) or all(
                    isinstance(x, bool) for x in values):
                pass
            else:
                values_2 = [float(i) for i in values]
                values = values_2
            if len(values) == self.length_array :
                self.elements = []
                for x in values:
                    self.elements.append(x)
            else:
                raise ValueError("Number are not equal to the size specified")
        else:
            raise TypeError("Elements are not of allowed type: float, int and bool")

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """

        i = 0
        str = ""
        for x in range(self.length_array):
            if i == self.shape_rows:
                str += "\n"
                i = 0
            str += f"{self.elements[x]}   "
            i += 1
        return str

    def __getitem__(self, index):
        """

        Retrives element at given index

        Args:
            index:
                - tuple(n,m): For n dimensional arrays. n is column index and m is row index
                - int: For one dimensional arrays

        Returns:
            int, bool, float: element at the given index

        Raises:
            ValueError: If the index is outh of bounds
        """
        if isinstance(index, tuple):
            if isinstance(index[0], int) and isinstance(index[0], int):
                n = index[0]
                m = index[1]
                if 0 <= n < self.shape_columns:
                    if 0 <= m < self.shape_rows:
                        if n == 0:
                            return self.elements[m]
                        else:
                            return self.elements[(n*self.shape_rows) + m]
                    else:
                        raise ValueError("Index is out of bounds")
                else:
                    raise ValueError("Index is out of bounds")
            else:
                raise TypeError("Index error, you can only retrive indexes with int")
        elif isinstance(index, int):
            if 0 <= index < self.shape_rows*self.shape_columns:
                return self.elements[index]
            else:
                raise ValueError("Index is out of bounds")


    def __add__(self, other):
        """
        Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        new_array = []
        if type(other) == Array:
            if other.shape_rows == self.shape_rows and other.shape_columns == self.shape_columns:
                for x in range(self.length_array):
                    add = self.elements[x] + other[x]
                    new_array.append(add)
            else:
                raise ValueError("The shape of the matrices are not equal.")
        elif type(other) == int or type(other) == float:
            for x in range(self.length_array):
                add = self.elements[x] + other
                new_array.append(add)
        else:
            return NotImplemented

        return Array(self.shape, *new_array)

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)


    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        new_array = []
        if type(other) == Array:
            if other.shape_rows == self.shape_rows and other.shape_columns == self.shape_columns:
                for x in range(self.length_array):
                    add = self.elements[x] - other[x]
                    new_array.append(add)
            else:
                raise ValueError("The shape of the matrices are not equal.")
        elif type(other) == int or type(other) == float:
            for x in range(self.length_array):
                add = self.elements[x] - other
                new_array.append(add)
        else:
            return NotImplemented

        return Array(self.shape, *new_array)


    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        new_array = []
        if type(other) == int or type(other) == float:
            for x in range(self.length_array):
                add = other - self.elements[x]
                new_array.append(add)
        else:
            return NotImplemented

        return Array(self.shape, *new_array)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        new_array = []
        if type(other) == Array:
            if other.shape_rows == self.shape_rows and other.shape_columns == self.shape_columns:
                for x in range(self.length_array):
                    add = self.elements[x] * other[x]
                    new_array.append(add)
            else:
                raise ValueError("The shape of the matrices are not equal.")
        elif type(other) == int or type(other) == float:
            for x in range(self.length_array):
                add = self.elements[x] * other
                new_array.append(add)
        else:
            return NotImplemented

        return Array(self.shape, *new_array)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        if type(other) == Array:
            if other.shape_rows == self.shape_rows and other.shape_columns == self.shape_columns:
                return True
            else:
                return False
        else:
            return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """

        if type(other) == Array:
            if self.__eq__(other):
                if self.elements == other.elements:
                    return True
                else:
                    return False
            else:
                raise ValueError("The matrices are not identical")
        elif type(other) == int or type(other) == float:
            bool_list = []
            for x in self.elements:
                if x == other:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return Array(self.shape, *bool_list)
    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """

        return min(self.elements)


if __name__ == "__main__":
    shape = (4 ,2)
    # define my_array
    my_array = Array(shape,2,3,1,0,2,3,4,5)
    print(my_array[(1,1)])
    test_a = Array((4,), 2, 3, 1, 0)
    test_b = test_a + 1.2
    print(str(test_b))
