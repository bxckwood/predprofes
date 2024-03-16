import csv

def insertion(data):
    """

    Принимает массив, Котоый необходимо отсортировать, затем сортирует вставками.

    """

    for i in range(len(data)):
        j = i - 1
        key = data[i]
        while int(data[j][1]) < int(key[1]) and j >= 0:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

def main():
    """

    F - открытие файла с кодировкой utf-8
    c - массив со всеми строками csv файла
    onlyFirstIndex - словарик в котором ключ - название зелья, значение - количество этого зелья
    onlyFirstIndexSp - отсортированный массив в котором первый индекс - это название зелья, а второй индекс - это ключ.

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
    onlyFirstIndexSp = [[i, onlyFirstIndex[i]] for i in onlyFirstIndex.keys()]
    onlyFirstIndexSp = insertion(onlyFirstIndexSp)
    onlyFirstIndexSp = onlyFirstIndexSp[::-1]

    for i in range(5):
        print(f"Зелья {onlyFirstIndexSp[i][0]} осталось {onlyFirstIndexSp[i][1]}")

main()