# def generator(num):
#     print('start')
#     while num>0:
#         yield num
#         num -=1
#
# val = generator(10)
# for x in val:
#     print(x)
#



def gener():
    f = open('input.txt', 'r')
    for x, line in enumerate(f):
        if 'error' in line:
            yield x
for c in gener():
    print(c)



