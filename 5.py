import csv

def main():
    """

    F - открытие файла с кодировкой utf-8
    c - массив со всеми строками csv файла
    allIngridiens - всевозможные ингрилидиенты
    allIngridients - кол-во повторений ингридиентов в зельях
    allIngridienetsMaxValues - максимальные значения повторений ингридиентов

    """
    F = open("magical.csv", encoding="utf-8")
    c = [i for i in csv.reader(F, delimiter=",")]
    c.pop(0)
    allIngridiens = []
    for i in c:
        allIngridiens.append(i[2])
        allIngridiens.append(i[3])
        allIngridiens.append(i[4])
    allIngridiens = list(set(allIngridiens))
    allIngridients = {i: 0 for i in allIngridiens}
    for i in c:
        allIngridients[i[2]] += 1
        allIngridients[i[3]] += 1
        allIngridients[i[4]] += 1
    allIngridientsMaxValues = sorted(set(allIngridients.values()))[::-1]
    allIngridientsMaxValues = allIngridientsMaxValues[:5]
    a = 0
    for i in allIngridientsMaxValues:
        for j in allIngridiens:
            if a == 5:
                break
            if allIngridients[j] == i:
                a += 1
                print(f"{j} - {i}")


main()