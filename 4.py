import csv

def main():
    """

    F - открытие файла с кодировкой utf-8
    c - массив со всеми строками csv файла
    allClasses - всевозможные классы
    allClassesSet - всевозможные классы без дупликатов
    allClaasesSet - кол-во повторений класса


    """

    F = open("magical.csv", encoding="utf-8")
    c = [i for i in csv.reader(F, delimiter=",")]
    c.pop(0)
    allClasses = []

    for i in c:
        if len(i[0].split(" ")) == 3:
            allClasses.append(i[0].split(" ")[1] + " " + i[0].split(" ")[2])
        if len(i[0].split(" ")) == 2:
            allClasses.append(i[0].split(" ")[1])

    allClasses = list(set(allClasses))
    allClassesSet = {i: [] for i in allClasses}
    allClassesSetKol = {i: 0 for i in allClasses}
    for i in c:
        for j in allClasses:
            if j in i[0]:
                if i[0] in allClassesSet[j]:
                    break
                else:
                    allClassesSet[j].append(i[0])
                    break

    for i in c:
        for j in allClasses:
            if j in i[0]:
                if int(i[1]) == -1:
                    break
                else:
                    allClassesSetKol[j] += int(i[1])
    for i in allClasses:
        print(f"{len(allClassesSet[i])} зелий класса {i}, общее количество зелий {allClassesSetKol[i]}")
main()