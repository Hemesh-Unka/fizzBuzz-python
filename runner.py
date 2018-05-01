from fizzbuzz import FizzBuzz

class Runner:

    def __init__(self, fizz_buzz_class = FizzBuzz):
        self.fizz_buzz_class = fizz_buzz_class

    def printer(self, x):
        numbers = list(range(1, x))
        for n in numbers:
            self.fizz_buzz_class.fizzBuzz(self, n)
            self.fizz_buzz_class.fizz(self, n)
            self.fizz_buzz_class.buzz(self,n)
            self.fizz_buzz_class.number(self, n)
