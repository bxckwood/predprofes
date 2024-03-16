import csv

def main():
    """

    F - открытие файла с кодировкой utf-8
    c - массив со всеми строками csv файла
    a - строка, в которую записывается ингридиент
    maxKolvo - максимальное количество зелья zelenie, с 3 третьим ингридиентом a
    zelenie - зелья с 3 ингридиентом a
    f - флаг, который отвечает нашли ли мы этот ингридиент ли вообще


    """


    F = open("magical.csv", encoding="utf-8")
    c = [i for i in csv.reader(F, delimiter=",")]
    c.pop(0)
    while True:
        a = input()
        if a == "стоп":
            break
        else:
            f = False
            maxKolvo = 0
            zelenie = ""
            for j in c:
                if a == j[4]:
                    f = True
                    if int(j[1]) > maxKolvo:
                        maxKolvo = int(j[1])
                        zelenie = j[0]
            if f == True:
                print(f"По вашему запросу {a} найден следующий вариант: {a} используется в {zelenie}, его количество составляет : {maxKolvo}")
                continue
            else:
                print("Такую траву мы не используем")
                continue


main()