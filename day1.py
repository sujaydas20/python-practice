a = [1, 2]
b = [a, a]

b[0].append(3)

print(a)
print(b)




d = {1: 10, 2: 20, 3: 30}

x = d.pop(2)
d[4] = x + d[3]

print(sum(d.values()))



s = 0

for i in range(1, 5):
    for j in range(1, 5):
        if i + j > 5:
            continue
        s += i * j

print(s)




def f(x, a=[]):
    a.append(x)
    return a

print(f(1))
print(f(2))
print(f(3))



def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return f(n-1) + 1
    return f(n-2) + 2

print(f(6))




a = [[1, 2, 3], [4, 5, 6]]

b = [
    x + y
    for x in a[0]
    for y in a[1]
    if (x + y) % 2 == 0
]

print(b)



def f(*args):
    if len(args) == 1:
        return args[0]
    return args[0] + f(*args[1:])

print(f(2, 4, 6, 8))



d = {"a": 1, "b": 2, "c": 3}

for k in d:
    if d[k] % 2 == 1:
        d[k] *= 2

print(d)


from functools import reduce

a = [1, 2, 3, 4]

x = reduce(lambda p, q: p * q, a)

print(x)


s = "COMPUTER"

a = s[1:7:2]
b = s[-2:1:-2]

print(a)
print(b)



def f(n):
    if n == 0:
        return 0
    return f(n-1) + n

print(f(5) - f(3))



a = [1, 2, 3, 4, 5]

b = [x*x if x % 2 == 0 else x+1 for x in a]

print(b)