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