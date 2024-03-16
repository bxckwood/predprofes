import csv


def main():
    """
    Описание функции main

    F - открытый файл с кодировкой utf-8
    c - массив со всеми данными
    onlyFirstIndex - словарь со всеми названиями без дупликатиов
    txttt - открытие файла с будущим его записыванием

    """

    F = open("magical.csv", encoding="utf-8")
    c = [i for i in csv.reader(F, delimiter=",")]
    c.pop(0)
    onlyFirstIndex = {i: 0 for i in list(set([i[0] for i in c]))}
    for i in c:
        if int(i[1]) == -1:
            continue
        else:
            onlyFirstIndex[i[0]] += int(i[1])

    print(f"Данного зелья осталось - {onlyFirstIndex["Мощное Зелье"]}")

    with open("magicaPotions.txt", "w", encoding="utf-8") as txttt:
        for i in onlyFirstIndex.keys():
            txttt.write(f"{i} в запасах еще есть - {onlyFirstIndex[i]}" + '\n')




main()