# 🛑
# breaks the nearest for or while loop

# 💕 check the number

# num = int(input())
# flag = True

# for i in range(2, num):
#     if (
#         num % i == 0
#     ):  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flad = False
#         break  # останавливаем цикл если встретили делитель числа

# if flag:  # эквивалентно if flag == True:
#     print("The number is prime")
# else:
#     print("The number is composite")

# ❗❗❗ Простые числа: 2, 3, 5, 7, 11, 13, 17 и т.д.
# Составные числа: 4 (делится на 1, 2 и 4), 6 (делится на 1, 2, 3 и 6), 8 (делится на 1, 2, 4 и 8)

# ❗❗❗ Оператор прерывания цикла break позволяет ускорять программы, так как мы избавляемся от лишних итераций.

# 💕 A program using a for loop that reads 10 numbers and adds them up until it finds a negative number. In this case, the execution of the loop is interrupted by the break command

# Программа с циклом for, которая считывает 10 чисел и суммирует их до тех пор, пока не обнаружит отрицательное число. В этом случае выполнение цикла прерывается командой break

# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
# print(result)

# ❗❗❗ Оператор прерывания цикла break удобен в связке с сигнальными метками: когда после проверки некоторого условия нам нет смысла продолжать выполнение цикла.

# 💕 If there is 7

num = int(input())
number = num
flag = False

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        flag = True
        break  # прерываем цикл, так как число гарантированно содержит цифру 7
    num //= 10

if flag:  # эквивалентно if flag == True:
    print("there is 7")
else:
    print("there's no 7")
# Как только мы встретили цифру 7, мы меняем значение сигнальной метки и прерываем цикл с помощью оператора break
