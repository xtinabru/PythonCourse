# WHILE  🪢

# There are counting (for) and conditional (while) loops.

# while условие:
#    блок кода

# i = 0
# while i < 10:
#     print("Привет")
#     i += 1

# Напишем программу, которая считывает числа и выводит их квадраты, пока не будет введено −1. При такой постановке задачи мы не можем воспользоваться циклом for, так как не знаем, сколько чисел будет предшествовать числу −1.

# num = int(input())

# while num != -1:
#     print("Square equals", num * num)
#     num = int(input())

# Цикл while очень похож на условный оператор if. Разница заключается в том, что в случае с условным оператором соответствующий блок кода будет выполняться только один раз, тогда как с циклом while блок кода будет выполнен многократно.


# FOR VS WHILE  🧙🏻‍♂️

# 1 print numbers from 1 to 100

# for i in range(101):
#     print(i)

# or

# i = 0
# while i < 101:
#     print(i)
#     i += 1

# 2 program that prints all numbers that are multiples of 3

# for i in range(0, 100, 3):
#     print(i)

# or

# i = 0
# while i < 100:
#     print(i)
#     i += 3

# Если заранее не известно количество итераций, то необходимо использовать цикл while и только его.


# Read data till stop value 🏊🏻‍♀️

# text = input()

# total = 0

# while text != "stop":
#     total += int(text)
#     text = input()

# print("Sum equals", total)

# Endless cycle 🤸🏼
# i = 0
# total = 0
# while i < 10:
#     total += i


# # исправление

# i = 0        # Инициализация счетчика итераций
# total = 0    # Инициализация переменной для накопления суммы

# while i < 10:  # Цикл выполняется, пока i меньше 10
#     total += i  # Добавляем текущее значение i к total
#     i += 1      # Увеличиваем значение i на 1 в каждой итерации

# print(total)   # Выводим итоговую сумму
