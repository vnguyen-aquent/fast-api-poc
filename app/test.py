'''
This code snippet demonstrates the use of a variable that is not utilized within the program.
'''

class Calculator:
    '''A simple calculator class with unused variable in add method'''
    def add(self, a, b):
        '''Add two numbers and return the result'''
        unused_variable = 42
        return a + b

    def add_two(self, a, b):
        '''Add two numbers and return the result'''
        unused_variable = 42
        return a + b
