"""1) Есть обычная функция
def hello(x):
print(x * x - 10)
Превратите данную функцию в lambda функцию
"""
lambda_funct=lambda x:x*x-10
print(lambda_funct(5))
"""2) Есть список name = [“Kuma”, “Nurtilek”, “Zina”, “Edzen”, “Kuma”, “Aitenur”, “Zina” ]
Уберите дубликаты с данного листа с помощью lambda функций
"""
names=set(['Kuma','Nurtilek', 'Zina', 'Edzen', 'Kuma', 'Aitenur', 'Zina' ])
names=list(names)
lambda_function=lambda names:names
print(lambda_function(names))
"""3) Есть список numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Выведите с помощью lambda функции чётные числа с списка
"""
print(list(filter(lambda number:number%2==0,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
"""4) names = [“azat”, “zina”, “kuma”, “anna”, “sas”]
Вывести с помощью lambda функции имена палиндромы"""
print(list(filter(lambda name: name==name[::-1],['azat', 'zina', 'kuma', 'anna', 'sas'])))
"""ДОП ЗАДАЧА:
5) Дайте пользователю ввести две отметки времени вместе с секундами. Ваша
программа должна найти разницу между двумя отрезками времени и вывести
на экран в секундах.
Условие: Первая отметка должна быть раньше по времени чем вторая.**
Пример:
1-ввод: 10:00:30
2-ввод: 15:05:09
Ответ: 18 279 секунд разница"""
hours1=int(input("Введите сколько часов:"))
minutes1=int(input("Введите сколько минут:"))
seconds1=int(input("Введите сколько секунд:"))
hour1_minutes1=hours1*60
minutes1_second1=hour1_minutes1+minutes1
minutes1_second1=minutes1_second1*60
second1=minutes1_second1+seconds1
hours2=int(input("Введите сколько часов:"))
minutes2=int(input("Введите сколько минут:"))
seconds2=int(input("Введите сколько секунд:"))
hour2_minutes2=hours2*60
minutes2_second2=hour2_minutes2+minutes2
minutes2_second2=minutes2_second2*60
second2=minutes2_second2+seconds2
print(second2-second1,"секунд разница")


