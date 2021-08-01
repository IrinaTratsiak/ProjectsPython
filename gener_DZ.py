n = int(input('задай количество чисел Фибоначчи '))
def fibonacchi(n):
    a, b = 0, 1
    l = []
    for i in range(n):
        a, b = b, a + b
        l.append(a)
    yield l
print(l)
