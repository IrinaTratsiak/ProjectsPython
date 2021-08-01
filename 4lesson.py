fruits = ['apple', 'bananas', 'mango']
new_list1 = [x for x in fruits if x[0] == 'a']
print(new_list1)

new = []
for x in fruits:
    if x[0] == 'b':
        new.append(x)
print(new)

n = 12
d = {}
for x in range(1, n+1):
    d.update({x: x**2})

d = {x: x**2 for x in range(1, n+1)}
print(d)

def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

d = lambda a, b,c: (a**2 - 4*b*c) ** 0.5
print(d(1, 2, -3))





