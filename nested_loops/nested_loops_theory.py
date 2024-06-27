# Nested loops 🪺 🐣 🌱


# Step 1 ⏰ seconds

# for seconds in range(60):
#     print(seconds)

# Step 2 ⏰ minutes

# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ":", seconds)

# Step 3 ⏰ hours

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# ❗❗❗

# вложенный цикл выполняет все свои итерации для каждой отдельной итерации внешнего цикла;

# вложенные циклы завершают свои итерации быстрее, чем внешние циклы;

# для того, чтобы получить общее количество итераций вложенного цикла, надо перемножить количество итераций всех циклов.

#  Мы можем вкладывать друг в друга циклы как for, так и while.


# Break and continue operators in nested loops 🪺 🐣 🌱

# 🟢 Оператор break выполняет прерывание ближайшего цикла в котором он расположен.

# 🟢 Оператор continue осуществляет переход на следующую итерацию ближайшего цикла.

# for i in range(3):
#     for j in range(3):
#         print(i, j)

# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2


# for i in range(3):
#     for j in range(3):
#         if i == j:
#             break
#         print(i, j)

# 1 0
# 2 0
# 2 1

# for i in range(3):
#     for j in range(3):
#         if i == j:
#             continue
#         print(i, j)


# 0 1
# 0 2
# 1 0
# 1 2
# 2 0
# 2 1

# 🔔 Если необходимо добиться прерывания внешнего цикла из-за выполнения условия во внутреннем, то стоит сделать это через сигнальную метку.


# Ex 1 💚

# ******
# ******
# ******
# ******
# ******
# ******
# ******
# ******

# for i in range(6):
#     print("*", end="")

# Для того чтобы завершить весь вывод таблицы звездочек, нам нужно выполнить этот цикл восемь раз. Мы можем поместить этот цикл в еще один цикл, который делает восемь итераций

# for i in range(8):
#     for i in range(6):
#         print("*", end="")
#     print()

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********

# for i in range(8):
#     for j in range(i + 1):
#         print("*", end="")
#     print()
