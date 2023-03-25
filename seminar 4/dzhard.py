# *****Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами

# Input -> 435467
# Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь

def number_to_words(n):
    units = ['', 'один', 'два', 'три', 'четыре',
             'пять', 'шесть', 'семь', 'восемь', 'девять']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
            'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста',
                'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'тысяча', 'тысячи', 'тысяч']
    millions = ['', 'миллион', 'миллиона', 'миллионов']

    if n == 0:
        return 'ноль'
    if n < 0:
        return 'минус ' + number_to_words(abs(n))

    words = ''
    if n // 1000000 > 0:
        millions_digit = n // 1000000
        millions_word = number_to_words(
            millions_digit) + ' ' + millions[get_form(millions_digit)]
        words += millions_word + ' '
        n %= 1000000

    if n // 1000 > 0:
        thousands_digit = n // 1000
        thousands_word = number_to_words(
            thousands_digit) + ' ' + thousands[get_form(thousands_digit)]
        words += thousands_word + ' '
        n %= 1000

    if n // 100 > 0:
        hundreds_digit = n // 100
        hundreds_word = hundreds[hundreds_digit]
        words += hundreds_word + ' '
        n %= 100

    if n >= 10 and n <= 19:
        words += units[n % 10] + 'надцать'
    else:
        if n // 10 > 0:
            tens_digit = n // 10
            tens_word = tens[tens_digit]
            words += tens_word + ' '
            n %= 10
        if n > 0:
            units_word = units[n]
            words += units_word

    return words.strip().capitalize()

# Функция возвращает форму слова для разрядов тысяч и миллионов


def get_form(n):
    if n % 10 == 1 and n % 100 != 11:
        return 1
    elif 2 <= n % 10 <= 4 and n % 100 < 10 or n % 10 == 0 or 5 <= n % 10 <= 9 or (11 <= n % 100 <= 14):
        return 3
    else:
        return 2


print(number_to_words(1234567))
