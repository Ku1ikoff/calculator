# Здесь можно тестировать функционал и писать мусорный код

def calculator(func):
    return func


def plus(*args):
    count = 0
    for i in args:
        count += i
    print(count)


calculator(plus(1, 2, 3, 4))
