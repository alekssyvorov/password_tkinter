# s = "Hello World!"
# new = s.lower()
# print(new)
# new = s.upper()
# print(new)
# print(s)
# s = "hELLO world!"
# print(s.title())
# # s = input('Y/N').upper()
# s = "hELLO world!"
# print(s.capitalize())
# print(s.swapcase())
# s = "Hello World!"
# print(s.count('T'))
#
# print(s.index('W'))
# print(s.index('o', 5, 8))
# # print(s.index('A'))
# print(s.rindex('d'))
# print(s.index('d'))
# s = "Hello World!"
# print(s.replace('e', 'i'))
# print(s.replace('l', 'L', 2))
#
# path = "C:\Windows\Help\OEM\IndexStore"
#
# path = path.replace('\\', '/')
# print(path)
# s = "Hello"
# new = s.center(20, "#")
# print(new)
# print(len(new))
# new = s.ljust(20, "$")
# print(new)
# print(len(new))

# path = "C:\Wiiiindows\Help\OEM\HndexStore"

# print(path.find('H', 12))
# print(path.find('A'))
# print(path.find('H', path.find('H')+1))
# print(path.rfind("H"))
# path = "C:\Wiiiindows\Help\OEM\HndexStore.png"
# print(path.startswith("C:"))
# print(path.startswith("D:"))
# path = "C:\Wiiiindows\Help\OEM\HndexStore.png"
# print(path.endswith('.png'))
# print(path.endswith('.jpg'))

s = '0123456789'
#06784563214
# print(s.isdigit())
# print(s.isnumeric())

# s = '  QWERTY1   '
# # s = s.strip()
# # s = s.lstrip()
# s = s.rstrip()
# print(s)
# print(s.isdigit())
# print(s.isnumeric())
# print(s.isalpha())
# print(s.isupper())
# print(s.isalnum())
# s = "Hello World!"
# s = s.replace(' ', '')
# s = s[:-1]
# s = s[:len(s)]
# print(s.isalpha())
# print(s)
# s = "        "
# print(s.isspace())
s = "Hello-world-!"
# print(s.istitle())

# new = s.split('-')
# print(new)
# s = '10.2'
# print(s.isdecimal())
# s = "Hello\t\tworld!"
# print(s)
#
# print(s.expandtabs(tabsize=12))
s = "Hello world!"
print(s.zfill(20))

# Пользователь вводит с клавиатуры строку. Произведите
# поворот строк и полученный результат выведите
# на экран.

# s = 'start' # -> 'trats'
# # 5
# for i in range(-1, (len(s)*(-1)-1), -1):
#     print(s[i], end='')
# print()
# print(s[::-1])
# Пользователь вводит с клавиатуры строку. Посчитайте
# количество букв, цифр в строке. Выведите оба
# количества на экран.

# s = input('Input s ') # f4sdf4sd4fgg45t
# count_alpha = 0
# count_number = 0
# for elem in s:
#     if elem.isalpha():
#         count_alpha += 1
#     elif elem.isdigit():
#         count_number += 1
#
# print('Symbol', count_alpha, 'Number', count_number)
st = input('Input string ')
symbol = input('Input symbol ')
count = 0
for elem in st:
    if elem == symbol:
        count += 1
print(count)
print(st.count(symbol))