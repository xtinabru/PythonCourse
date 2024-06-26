# Infinite loops 🌠

# example 1 🟡

# while True:
#    print('Python is awesome!')

# example 2 🟡

# while True:
#     query = get_new_query() #  получаем новый запрос на обработку
#     query.process()         #  обрабатываем запрос

# example 2 🟡
# while True:
#     if условие 1:  # условие для остановки цикла
#         break
#     ...
#     if условие 2:  # еще одно условие для остановки цикла
#         break
#     ...
#     if условие 3:  # еще одно условие для остановки цикла
#         break

# CONTINUE 🟣 🟣 🟣

# Оператор continue позволяет перейти к следующей итерации цикла for или while до завершения всех команд в теле цикла.

# Программа, которая выводит все числа от 1 до 100, кроме чисел 7, 17, 29 и 78.

# ➰➰➰
# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  #  go to the next iteration
#     print(i)

# 🔔 NOTA BENE

#  🟡 Оператор break прерывает выполнение ближайшего цикла, а не программы, то есть далее будет выполнена команда, следующая сразу за циклом.
