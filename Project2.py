import calendar

month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
odd = 172
even = 168
leap = 165
notLeap = 154
year = int(input("Введите год: "))

for i in range(12):
    if (i)%2 == 0:
        print(f"{month[i]}: {odd}")
    else:
        if i == 1:
            if (calendar.isleap(year)):
                print(f"{month[i]}: {leap}")
            else:
                print(f"{month[i]}: {notLeap}")

        else:
            print(f"{month[i]}: {even}")