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