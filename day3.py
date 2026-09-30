def dec(f):
    def wrapper(x):
        return f(x) + 2
    return wrapper

@dec
def calc(x):
    return x * 3

print(calc(4))