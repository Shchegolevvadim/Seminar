from fractions import Fraction
x = Fraction(1,3)
y = Fraction(1,2)
def init(a, b):
    global x
    global y 
    x = a
    y = b
def do_it():
    return x * y