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