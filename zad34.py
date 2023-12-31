# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
# если с ритмом все не в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам


def ritm_text(text):
    phrases = text.split(" ")  # бьем текст на фразы по пробелам d список
    if (
        len(phrases) <= 1
    ):  # если не задано текста или одна фраза - считаем неудачным стихом
        return False
    vowels = {"а", "о", "у", "е", "и", "ы", "э", "ю", "я", "ё"}  # множество гласных
    syllables = []  # слоги - считаем гласные по фразам и заносим в список
    for i in range(len(phrases)):  # бьем фразы на слоги по гласным
        print(phrases[i])
        isit = 0  # сколько слогов
        for j in phrases[i]:
            print(j)
            if j in vowels:
                isit += 1  # является ли гласной
        syllables.append(isit)  # сколько слогов во фразе

    test = syllables[0]
    for j in range(1, len(syllables)):  # сравниваем количество слогов по фразам
        if syllables[j] != test:
            return False
    return True


test_text = input("Введите фразу Винни-Пуха: ")
if ritm_text(test_text) == True:
    print("Парам пам-пам")
else:
    print("Пам парам")
