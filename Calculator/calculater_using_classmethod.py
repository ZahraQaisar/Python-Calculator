'''     OOP
class - blueprint to create objects
        attributes (variables)
        methods (funtions)

object (instance)

buit in function
__init__() - initialize
self - bydefault called; the object itself

when return 'object' is returned.

* regular methods - first instance is self

* class methods - @classmethod before function 
                - when the whole class is needed as a 1st parameter
                - alternative contructors
              
* static methods - @staticmethod
                 - no self instance
                 - no class'''
                 
from math import sqrt
class Calculate:
    def __init__(self, op, n1=0, n2=0):
        self.num1 = n1
        self.num2 = n2
        self.op = op
        self.fac = 1
    
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def product(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by 0."
    
    def exponent(self):
        return self.num1 ** self.num2  
    
    def sqaure_root(self):
        return sqrt(self.num1)
    
    def factorial(self):
        if(self.num1 <= 0):
            print('no factorial for', self.num1)
        else:
            for i in range(self.num1, 0, -1):
                self.fac = self.fac * i
            return self.fac
    
    def display(self):
        print('num1:',self.num1, ', Operator:', self.op, ', num2:', self.num2)
        if self.op == '+':
            print('Addition: ', c1.add())
        elif self.op == '-':
            print('Subtraction: ', c1.sub())
        elif self.op == '*':
            print('Product: ', c1.product())
        elif self.op == '/':
            print('Division: ', c1.division())
        elif self.op == '^':
            print('Exponent: ', c1.exponent())
        elif self.op == '!':
            print('Factorial: ', c1.factorial())
        elif self.op == '|':
            print('Square root: ', c1.sqaure_root())
    
    @classmethod 
    def fromString(cls, str_input):
        operators = ['+', '-', '*', '/','^', '!', '|']
        for x in operators:
            if x in str_input:
                num1,num2 = str_input.split(x)
                if (num1 != '' and num2 != ''):
                    return cls(x, int(num1), int(num2))
                    quit()
                elif (num1 == ''):
                    return cls(x, int(num2))
                    quit()
                elif(num2 == ''):
                    return cls(x, int(num1))
                    quit()
                    

str_input = input("Enter values and operator in fomat(a+b)(for sqaure root use '|'):")
c1 = Calculate.fromString(str_input)
c1.display()