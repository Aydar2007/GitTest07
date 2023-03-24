#Задание1) Даны два словаря: dictionary_1 = {'a': 300, 'b': 400} и dictionary_2 = {'c': 500, 'd':600}. Объедините их в один при помощи встроенных функций языка Python.Подсказка: метод update()
# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd':600}
# # dictionary_1.update(dictionary_2)
# print(dictionary_1)
#Задание2) Дан словарь с числовыми значениями. numbers = {‘num_1’ : 1, ‘num_2’ : 2, ‘num_3’ : 3, ‘num_100’ : 100} Необходимо умножить все числовые значения словаря на 5 и вывести в терминал
# numbers = {"num_" : 1, "num_2" : 2, "num_3" : 3, "num_100" : 100}
# numbers1={"num_1":1*5, "num_2" : 2*5, "num_3" : 3*5, "num_100" : 100*5}
# print(numbers1)
#Задание3) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Умножьте его age на 2 раза
# student = {"name" : "Askhat", "age" : 17}
# age=(17*2)
# print(age)
# student["age"]=age
# print(student)
#Задание4) Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17, ‘color’ : ‘White’}. Обновите age в 16
# student = {"name" : "Askhat", "age" : 17, "color" : "White"}
# student["age"]=16
# print(student)
#Задание5)Есть словарь student = {‘name’ : ‘Askhat’, ‘age’ : 17}. Удалите ключ и значение age
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop("age")
# print(student)
#Задание6)Есть словарь student = {‘name’ : ‘Askhat’}. Добавьте новый ключ(address) и значение(Западный Анар)
# student = {'name' : 'Askhat'}
# student.setdefault("address","Западный Анар")
# print(student)
#Доп.задание7) Напишите программу, которая имитирует проверку пароля, придуманного пользователем. Пользователь вводит пароль, а потом ещё раз его же, для подтверждения
while True:
    passwords={}
    password=(input("Придумайте пароль:"))
    if (len(password))>=8:
        print()
    else:
        print("Короткий пароль!!!")
        break
    if "123" in password:
        print("Пароль слишком простой")
        break
    password_1=(input("Введите пароль:"))
    password_2=(input("Подтвердите пароль:"))
    if password_1==password_2:
        print("Правильный пароль!!!")
    else:
        print("Различаются")
    if password_1==password_2:
        print("Ok")
    if password_1==password_2:
        passwords.setdefault("password_1",password_1)
    else:
        print("Неправильный пароль!!!")
    print(passwords)
"""И пароль который вводит пользователь записывается в пустое множество после проверок
Если первый пароль, который ввел пользователь короче 8 символов, программа
выводит на экран слово "Короткий пароль!" Если же первый пароль достаточно длинный, но в нём содержится сочетание
символов "123", программа выводит на экран слово "Простой пароль!Если же предыдущие проверки пройдены успешно, но введённые слова-пароли
не совпадают, то программа выводит на экран слово "Различаются."
Если же и третья проверка пройдена успешно, программа выводит "OK"
(латинскими буквами) и выводит “Пароль создан!”"""







