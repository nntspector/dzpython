# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Введите трехзначное число: '))
a = int(number/100)
b = int((number/10) % 10)
c = int(number % 10)
result = int(a+b+c)
print(number, '->', result, '(', a, '+', b, '+', c, ')')
