# #Задание1 +
# for i in range(1,6):
#     print(i,"0")

#Задание2 + Нужно заполнить пустой список от 1 до 100. Полученный результат вывести на экран. Подсказка: используйте функцию range() и пустой список
# a=[]
# for b in range(1,101,1):
#     a.append(b)
#     print(a)
#Задание3 + Вывести на экран все чётные значения в диапазоне от 1 до 497. Подсказка: используйте функцию range() или условия
# for c in range(1,497,1):
#     if c %2==0:
#         print(c)
#Задание4 +
# l=range(1,1001)
# print(max(l))
# print(min(l))
# print(sum(l))
#Задание5 +  Заполнить список ста нулями с помощью функции range()
# t=[]
# for t in range(100):       
#     for t in range(0,1):
#         print(t)
#Задание6 +
# it_company = ("Google", "Amazon", "Microsoft")
# it_company = (list(it_company))
# it_company.append("Tesla")
# it_company = (tuple(it_company))
# print(it_company)
#Задание7 + Из 6 задания попробуйте вывести индекс ‘Amazon’
# print(it_company.index("Amazon"))
#Задание8 + Из 1 задания обновите значение ‘Google’ на ‘Apple’ любыми способами
# it_company = (list(it_company))
# it_company.pop(0)
# it_company.insert(0,"Apple")
# print(it_company)
#Задание9 + Из 1 задания сделайте срез ‘Apple’ до ‘Microsoft’
# del it_company[0:4]
# print(it_company)
#Задание10 +
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
# 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
# 'overview')
# print(text_tuple.count("python"))# В условии python  с маленькой буквы  если python c маленькой буквы то таких слов в тексте 0
# print(text_tuple.count("Python"))#Ну а если Python с большой буквы то таких слов 2
#доп.задание + 6) Исходные значения двух переменных запросить у пользователя. Поменять значения переменных местами. Вывести новые значения на экран. Решите задачу, используя только две переменные.
# per1=int(input("Введите 1 переменую:"))
# per2=int(input("Введите 2 переменую:"))
# per3=per1
# per1=per2
# per2=per3
# print("1Переменная:",per1)
# print("2Переменная:",per2)
#доп.задание + 7) Создайте бесконечный цикл. Запросите у пользователя его возраст. Если ему есть 18 лет, выведите: "Доступ разрешен" и остановите цикл, иначе "Извините, пользование данным ресурсом только с 18 лет" и запросите заново
# while True:
#     years_old=(int(input("Укажите ваш возвраст:")))
#     if years_old >= 18:
#         print("Доступ разрешен")
#         break
#     else:
#         print("Извините, пользование данным ресурсом только с 18 лет")
#         continue





