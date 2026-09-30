class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.x += 5

b = B()

print(b.x)




class A:
    def value(self):
        return 10

class B(A):
    def value(self):
        return 2 * super().value()

class C(B):
    def value(self):
        return super().value() + 5

c = C()

print(c.value())


from collections import Counter

s = "BANANA"

c = Counter(s)

print(c["A"] + c["N"])


d = {}

d.setdefault("a", 10)
d.setdefault("a", 20)
d.setdefault("b", 30)

print(d["a"] + d["b"])


from collections import defaultdict

d = defaultdict(int)

for x in [1, 2, 1, 3, 2, 1]:
    d[x] += 1

print(d[1] * d[2] + d[3])




a = [1, 2, 3]
b = [4, 5, 6]

c = list(map(lambda x, y: x*y + y, a, b))

print(c[0] + c[2])



s = "GATE2027"

x = list(filter(str.isdigit, s))

print(len(x))


a = [1, 2, 3, 4, 5]

r = reversed(a)

print(next(r))
print(next(r))
print(next(r))





from collections import Counter

a = [2, 3, 2, 4, 3, 2, 4]

c = Counter(a)

print(c.most_common(2)[0][0])




a = [4, 7, 2, 9, 6]

s = 0

for i, x in enumerate(a):
    if i % 2 == 0:
        s += x

print(s)



keys = ["a", "b", "c"]
values = [2, 4, 6]

d = dict(zip(keys, values))

d["b"] += d["c"]

print(d["a"] + d["b"])


def dec(f):
    def wrapper(x):
        return f(x) + 2
    return wrapper

@dec
def calc(x):
    return x * 3

print(calc(4))