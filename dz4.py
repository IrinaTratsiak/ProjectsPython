squire = {
    'triangle' : 1,
    'rectangle' : 2,
    'circle' : 3
}
j =input("выберите фигуру ")
if squire.get(j) == 1:
    print("введите стороны треугольника")
    a, b, c = map(int, input().split())
    pp = (a +b +c)/2
    s =(pp * (pp -a) *(pp -b) *(pp-c)) **0.5
    print("площадь треугольника", s)
elif squire.get(j) == 2:
    print("введите стороны прямоугольника")
    d, e = map(int, input().split())
    print("площадь прямоугольника",d *e)
elif squire.get(j) == 3:
    print("введите радиус")
    r = int(input())
    print("площадь круга", 3.14 *r *r)
else:
    print("ошибка ввода")



