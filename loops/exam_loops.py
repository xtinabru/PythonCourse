# 1 range(6) ✏️

# for i in range(6):
#     print(i)

# 2 range(2, 6) ✏️

# for i in range(2, 6):
#     print(i)

# 3  range(0, 501, 100) ✏️

# for i in range(0, 501, 100):
#     print(i)

# 0
# 100
# 200
# 300
# 400
# 500

# 4  range(10, 5, -1) ✏️

# 10,9,8,7,6

# 5 ✏️

# for i in range(10, 25):
#     print("Python awesome!")

# 6 ✏️

# n = int(input())
# counter = 0

# for i in range(1, n + 1):
#     if i % 3 == 0 and i % 7 != 0:
#         counter += 1

# print(counter)

# выводит количество чисел от 1 до n кратных 3, но не кратных 7

# 7 ✏️ 7 раз

# i = 4
# while i <= 10:
#     print("Python!")
#     i += 1

# 8 ✏️

# n = int(input())
# res = 1
# i = 2
# while i <= n:
#     res *= i
#     i += 1
# print(res)
# выводит факториал числа n

# 9 ✏️

# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)
# выводит минимальный делитель числа, отличный от единицы

# REVIEW 7 🌶️

# WAS
# n = input()
# s = 0
# while n > 10:
#     if n % 2 == 1:
#         s = n % 10
#     n //= 10
# print(s)

# Ошибки в программе:

# n считывается как строка, а необходимо работать с числами, поэтому его нужно конвертировать в целое число.

# Условие while n > 10: не позволит обработать числа меньше или равные 10. Нужно использовать while n > 0:.

# Проверка на четность if n % 2 == 1: неверна, так как она проверяет на нечетность. Необходимо проверять четность if n % 10 % 2 == 0:.

# Внутри условия, s = n % 10 нужно складывать четные цифры, а не присваивать значение последней цифры.

# В строке n //= 10 уменьшаем число, чтобы работать с каждой цифрой по отдельности.

# n = int(input())
# s = 0
# while n > 0:
#     digit = n % 10
#     if n % 2 == 0:
#         s += digit
#     n //= 10
# print(s)


# REVIEW 8 🌶️

# На обработку поступает последовательность из 8 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**12.

# Нужно написать программу, которая выводит на экран количество делящихся нацело на 4 чисел в исходной последовательности и максимальное делящееся нацело на 4 число. Если делящихся нацело на 4 чисел нет, на экран требуется вывести «NO». Программист торопился и написал программу неправильно.

# Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

# was

# n = 7
# count = 0
# maximum = 1000
# for i in range(1, n + 1):
#     x = int(input())
#     if x // 4 == 0:
#         count += 1
#         if x < maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# CORRECT


# n = 8
# count = 0
# maximum = None

# for i in range(n):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if maximum is None or x > maximum:
#             maximum = x

# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# REVIEW 9 🪄

# На обработку поступает последовательность из 4 целых чисел. Известно, что вводимые числа по абсолютной величине не превышают 10**8.
# Нужно написать программу, которая выводит на экран количество нечетных чисел в исходной последовательности и максимальное нечетное число. Если нечетных чисел нет, требуется на экран вывести «NO». Программист торопился и написал программу неправильно.

# Найдите все ошибки в этой программе (их может быть одна или несколько). Известно, что каждая ошибка затрагивает только одну строку и может быть исправлена без изменения других строк.

# WAS

# n = 4
# count = 0
# maximum = 999
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = i
#             break
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# CORRECT

# n = 4
# count = 0
# maximum = None

# for i in range(n):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if maximum is None or x > maximum:
#             maximum = x

# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print("NO")

# Star frame 10 ⭐️⭐️⭐️

# На вход программе подается натуральное число n. Напишите программу, которая печатает звездную рамку размерами n X 19.

# n = int(input())

# for i in range(n):
#     for j in range(19):
#         if i == 0 or i == n - 1 or j == 0 or j == 18:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# 11 ⭐️⭐️⭐️

# There is n. n > 99. Find the 3rd number from the beggining.

# n = int(input())

# if n < 100:
#     print("Ошибка: Число должно быть больше 99.")
# else:
#     # Удаляем последние две цифры, чтобы осталась только третья цифра с начала
#     while n >= 1000:  # Пока у нас больше 3 цифр, удаляем последние
#         n //= 10

#     # Теперь n содержит число с тремя цифрами, третья цифра с начала будет в последней цифре
#     third_digit = n % 10

#     print(third_digit)

# ⭐️


# # OPTIONS
# n = int(input())
# while n > 999:
#     n //= 10

# print(n % 10)

# 12 ALL TOGETHER ⭐️⭐️⭐️

# There is number - n.
# Find: how many digits 3 are there in it.
# How many times the last digit is there.
# The quantity of even digits.
# the sum of its digits which > 5
# the multiplication of digits which > 7 ( if there are no 7, print 1, if there is only one digit print it)
# how many times there 0 and 5 (all together in sum)

# n = int(input())  # Чтение числа

# # Переменные для хранения результатов
# count_3 = 0
# count_last_digit = 0
# even_digits_count = 0
# sum_digits_greater_than_5 = 0
# digits_greater_than_7 = []
# count_0_and_5 = 0

# # Запоминаем последнюю цифру числа
# last_digit = n % 10

# # Переменная для хранения произведения цифр больше 7
# product_of_digits_greater_than_7 = 1
# found_digits_greater_than_7 = False

# # Обрабатываем цифры числа
# while n > 0:
#     digit = n % 10  # Получаем последнюю цифру
#     n //= 10  # Убираем последнюю цифру из числа

#     # Проверяем цифру на соответствие условиям
#     if digit == 3:
#         count_3 += 1

#     if digit == last_digit:
#         count_last_digit += 1

#     if digit % 2 == 0:
#         even_digits_count += 1

#     if digit > 5:
#         sum_digits_greater_than_5 += digit

#     if digit > 7:
#         digits_greater_than_7.append(digit)
#         found_digits_greater_than_7 = True

#     if digit == 0 or digit == 5:
#         count_0_and_5 += 1

# # Произведение цифр больше 7
# if found_digits_greater_than_7:
#     if len(digits_greater_than_7) == 1:
#         product_of_digits_greater_than_7 = digits_greater_than_7[0]
#     else:
#         from functools import reduce
#         from operator import mul
#         product_of_digits_greater_than_7 = reduce(mul, digits_greater_than_7)
# else:
#     product_of_digits_greater_than_7 = 1

# # Вывод всех результатов
# print(count_3)
# print(count_last_digit)
# print(even_digits_count)
# print(sum_digits_greater_than_5)
# print(product_of_digits_greater_than_7)
# print(count_0_and_5)

# Числа Рамануджана 13 🌶️

# for i in range(100000):

#     j1 = -1

#     k1 = -1

#     count = 0

#     for j in range(int(i ** (1 / 3)) + 1):

#         if j == k1:

#             continue

#         for k in range(int(i ** (1 / 3)) + 1):

#             if k == j1:

#                 continue

#             if i == j**3 + k**3:

#                 count += 1

#                 j1 = j

#                 k1 = k

#     if count >= 2:

#         print(i)
