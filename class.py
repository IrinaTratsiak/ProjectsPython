class A:
    def __init__(self, n):
        self.n = n
    def m1(self, x):
        print(x, self.n)

obj = A(5)
obj.m1(123)

class Animal:
    def __init__(self, color, voice):
        self.__color = color
        self.__voice = voice

    def say(self):
        print(self.__voice)

    @property
    def color(self):
        return self.__color

a = Animal('red', 'rrrr')
a.say()
print(a.color)
