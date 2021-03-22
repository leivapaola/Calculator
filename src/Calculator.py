from Subtraction import subtraction
from addition import addition
from Multiplication import multiplication
from Division import division
from Square import Square
from Square root import Squareroot


class Calculator:
    result = 0

    def __int__(self):
        pass

    def subtract(self, a,b):
        self.result = subtraction(a, b)
        return self.result

    def add(self, a,b):
        self.result = addition(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = squareroot(a)
        return self.result