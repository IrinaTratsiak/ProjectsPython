def validation(func):
    def wrapper(data):
        if isinstance(data, int) is False:
            data = str(data)
            print('не число, а строка')
        else:
            data = int(data)
            print('число')
    return wrapper


@validation
def schet(x):
    y = x +x
    print('result schet', y)
schet('er')
