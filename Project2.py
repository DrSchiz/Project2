import calendar

year = int(input("Введите год: "))
if (calendar.isleap(year)):
    feb = 29
else:
    feb = 28
month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
days = [31, feb, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]

def sumDigits(n):
    sum = 0
    while n!=0:
        sum += n%10
        n=n//10
    return sum

day = 0

for i in range(12):
    count = 0
    for a in range(days[i]+1):
        count += sumDigits(a)
    day += count
    print(f"{month[i]}: {count}")
print(f"Количество дней в году: {day}")