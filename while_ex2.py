# Ex 1 Till the end 1 💔🌹⚰️

# На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» (без кавычек). При этом само слово «КОНЕЦ» не входит в последовательность, лишь символизируя её окончание. Напишите программу, которая выводит члены данной последовательности.

# На вход программе подается последовательность слов, каждое слово на отдельной строке.

# text = input()

# while text != "КОНЕЦ":
#     print(text)
#     text = input()

# Ex 2 Till the end 2 💔🌹⚰️

# На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является слово «КОНЕЦ» или «конец» (большими или маленькими буквами, без кавычек). При этом сами слова «КОНЕЦ» и «конец» не входят в последовательность, лишь символизируя её окончание. Напишите программу, которая выводит члены данной последовательности.

# text = input()
# while text != "КОНЕЦ" and text != "конец":
#     print(text)
#     text = input()

# Ex 3  🙂‍↔️ 🧚‍♀️🧎‍♂️‍➡️

# На вход программе подается последовательность слов, каждое слово на отдельной строке. Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). Сами эти слова в последовательность не входят, лишь символизируя её окончание. Напишите программу, которая выводит общее количество членов данной последовательности.

# text = input()

# total = 0
# i = 1

# while text != "стоп" and text != "хватит" and text != "достаточно":
#     text = input()
#     total += i
# print(total)

# Ex 4 🟣

# n = int(input())

# while n % 7 == 0:
#     print(n)
#     n = int(input())


# Ex 5 The sum of numbers 🟢

# n = int(input())

# total = 0

# while n >= 0:
#     total += n
#     n = int(input())

# print(total)


# Ex 6 The quantity of 5

# n = int(input())

# total = 0
# while 0 < n <= 5:
#     if n == 5:
#         total += 1
#     n = int(input())

# print(total)

# Ex 7


# n = int(input())

# count = 0

# while n > 0:
#     if n >= 25:
#         count += n // 25
#         n %= 25
#     elif n >= 10:
#         count += n // 10
#         n %= 10
#     elif n >= 5:
#         count += n // 5
#         n %= 5
#     else:
#         count += n
#         n = 0

# print(count)

# or

# n = int(input())
# print (n // 25 + (n % 25) // 10 + (n % 25 % 10) // 5 + (n % 25 % 10 % 5))
