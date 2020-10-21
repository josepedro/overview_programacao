import sys

class Factorial:
    
    def __init__(self, number):
        self.number = number
        self.result = self.__compute(number)
    
    def __compute(self, number):
        return 1 if number == 0 else self.__compute(number - 1) * number

if __name__ == '__main__':
    try:
        number = int(sys.argv[1])
        result = Factorial(number).result
        print('The factorial of ' + str(number) + ' is ' + str(result) + ' .')
    except:
        print('You need to put a number as an argument of input.')

