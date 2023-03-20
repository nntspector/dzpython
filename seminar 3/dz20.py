# *Задача 20: * В настольной игре Скрабл (Scrabble)
# каждая буква имеет определенную ценность.
#  В случае с английским алфавитом очки распределяются
# так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка;
#  F, H, V, W, Y – 4 очка;
#  K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т
#  – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3
# очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
#  Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу,
#  которая вычисляет стоимость введенного пользователем слова.
#  Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.


word = (input('Введите слово на оценку: '))
char_1 = ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T',
          'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т')
char_2 = ('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У')
char_3 = ('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я')
char_4 = ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы')
char_5 = ('K', 'Ж', 'З', 'Х', 'Ц', 'Ч')
char_6 = ('J', 'X', 'Ш', 'Э', 'Ю')
char_7 = ('Q', 'Z', 'Ф', 'Щ', 'Ъ')
count = 0
for i in range(len(word)):
    for j in range(len(char_1)):
        if word[i] == char_1[j]:
            count += 1
for i in range(len(word)):
    for j in range(len(char_2)):
        if word[i] == char_2[j]:
            count += 2
for i in range(len(word)):
    for j in range(len(char_3)):
        if word[i] == char_3[j]:
            count += 3
for i in range(len(word)):
    for j in range(len(char_4)):
        if word[i] == char_4[j]:
            count += 4
for i in range(len(word)):
    for j in range(len(char_5)):
        if word[i] == char_5[j]:
            count += 5
for i in range(len(word)):
    for j in range(len(char_6)):
        if word[i] == char_6[j]:
            count += 8
for i in range(len(word)):
    for j in range(len(char_7)):
        if word[i] == char_7[j]:
            count += 10

print(f'стоимость вашего слова = {count}')
