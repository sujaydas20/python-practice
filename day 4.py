print("njvhsh")









def double(f):
    def wrapper(x):
        return f(x) * 2
    return wrapper

def add_three(f):
    def wrapper(x):
        return f(x) + 3
    return wrapper

@double
@add_three
def calc(x):
    return x + 1

print(calc(4))




class Counter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            raise StopIteration
        self.n -= 1
        return self.n

c = Counter(3)
print(list(c))








s = "gate-python-exam"
a, b, c = s.partition("-")

print(a + c)





class A:
    x = 5

    def update(self):
        self.x += 2

a = A()
b = A()

a.update()

print(A.x, a.x, b.x)




def first():
    yield 1
    yield 2

def second():
    yield 0
    yield from first()
    yield 3

print(list(second()))



class Number:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x % 3 == other.x % 3

a = Number(7)
b = Number(10)
c = Number(12)

print(a == b, b == c)





def calculate(x):
    try:
        result = 10 // x
    except ZeroDivisionError:
        return 100
    else:
        return result + 5

print(calculate(2) + calculate(0))




def calc(a, *, b=4):
    return a * b

print(calc(3) + calc(2, b=5))




a = [1, 2, 3]
b = a
c = a[:]

b[1] = 9
c[2] = 7

print(a, b, c)



class Item:
    def __str__(self):
        return "STR"

    def __repr__(self):
        return "REPR"

x = Item()
print(str(x), repr(x))






def f(n):
    if n <= 1:
        return 1
    return n * f(n - 2)

print(f(6))




a = [0, 2, 4, 6]

print(any(a), all(a), any(x % 2 for x in a))





class Calc:
    x = 10

    @staticmethod
    def add(a, b):
        return a + b

print(Calc.add(Calc.x, 5))





import math

a = math.gcd(24, 36)
b = math.lcm(4, 6)

print(a + b)