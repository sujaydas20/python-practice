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