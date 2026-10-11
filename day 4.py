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