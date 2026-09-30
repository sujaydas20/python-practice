def dec(f):
    def wrapper(x):
        return f(x) + 2
    return wrapper

@dec
def calc(x):
    return x * 3

print(calc(4))



class A:
    def __init__(self, x):
        self.x = x

    def __len__(self):
        return self.x * 2

a = A(4)
print(len(a))




import heapq

a = [7, 2, 9, 1, 5]
heapq.heapify(a)

print(heapq.heappop(a))
print(heapq.heappop(a))



def gen():
    x = 1
    while x < 5:
        yield x
        x += 2

g = gen()

print(next(g))
print(next(g))
print(list(g))