def s(a):
    if a[0] == '!':
        a = a.upper()
    else:
        a = a.lower()
    a = a.translate(str.maketrans('', '', '!@#%'))
    print(a)


while b := input():
    s(b)
# Необходимо написать программу, которая будет принимать на вход строки,
# преобразовывать и выводить их. Если первым символом в строке является “!”,
# то строку нужно привести к верхнему регистру, иначе к нижнему. Также из строки
# нужно удалить все символы “!”, “@”, “#”, “%”. Получившуюся строку нужно вывести.
# # Реализуйте функцию, которая будет принимать строку, обрабатывать ее по условиям
# # выше и возвращать обработанную строку в качестве результата. Полученную функцию
# # применяйте к строкам подаваемым на вход.
# Входные данные
#
# Hello World!
# !Python programming language
# Выходные данные
#
# hello world
# PYTHON PROGRAMMING LANGUAGE