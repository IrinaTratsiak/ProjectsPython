a = input()
b = input()
try:
    a = int(a)
    b = int(b)
    if a in range(3,23) and b in range(3,23):
        print(abs(a-b))
    else:
        print(a+b)
except ValueError:
    print(a+b)
