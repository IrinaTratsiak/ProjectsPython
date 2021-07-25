a, b, c = input().split()
try:
    d =(a +b +c)
    a = int(a)
    b = ("+", "-", "*", "/")
    c = int(c)
    if a in range(3,23) and c in range(3,23):
        print(eval(d))
    else:
        print("не входит в диапазон")
except:
    print("ошибка ввода данных")

