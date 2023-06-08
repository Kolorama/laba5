days = ("Пн", 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')
s = int(imput("Ввести кол-во выходных"))
for i in days:
    print("Рабочие ", days[:-s])
    print("Выходные", days[-s:])
    break