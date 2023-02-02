import numpy as np

# The class Tensor is a wrapper around a numpy array that allows us to add two tensors together
class Tensor(object):
    def __init__(self, data):
        """
        The function takes in a list of numbers and converts it to a numpy array
        
        :param data: a list of lists, each list is a row of the table
        """
        self.data = np.array(data)

    def __add__(self, other):
        """
        > The `__add__` function is a special function that is called when the `+` operator is used on two
        objects of the same type
        
        :param other: The other tensor to add to this one
        :return: A Tensor object with the data attribute being the sum of the data attributes of the two
        Tensor objects.
        """
        return Tensor(self.data + other.data)

    def __repr__(self):
        """
        It returns a string representation of the data in the node
        :return: The data is being returned.
        """
        return str(self.data.__repr__())

    def __str__(self):
        """
        The function takes a string and returns a string
        :return: The data is being returned as a string.
        """
        return str(self.data.__str__())
    

X = Tensor([1, 2, 3, 4, 5])
