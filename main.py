print("Добро пожаловать в калькулятор")

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))

user_operation = input("Введите знак операции: ")

operation = {
    "+": lambda num_1, num_2: num_1 + num_2,
}

result = operation[user_operation](number_1, number_2)
print(result)
