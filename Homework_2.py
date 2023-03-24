"""Задание-1Написать программу, которая будет проверять пароль. Пусть программа в начале
запросит пароль у пользователя. В самой программе сохраните определенный пароль
и сравните его с тем, который был введен пользователем. В случае, если пароли
совпадают, то выведете на экран следующее сообщение: ‘Password is correct. You are
welcome’ Если нет: ‘Password is incorrect. Please, try again’
Программу решить 2 способами, 4 строчной if else конструкцией и 1 строчной версией
if else."""
# 1.
# password=input("Password:")
# if password=="GEEKS":
#     print("Password is correct. You are welcome")
# else:
#     print("Password is incorrect. Please, try again")
# 2.
# password=input("Password:")
# print("Password is correct. You are welcome") if password=="GEEKS2023" else print("Password is incorrect. Please, try again")
'''ЗАДАЧА №2
Написать программу, которая будет спрашивать у пользователя температуру за окном.
Используя условные конструкции if elif else, напишите программу, которая выводит на
экран следующее:
1) При условии меньше -30 градусов: “Там так холодно, лучше дома сиди!”
2) При условии от -30 до 0: “Холодновато. Оденься потеплее!”
3) При условии от 0 до 15: “Прохладно. Куртку накинь!”
4) При условии от 15 до 30: “Тепло. Иди погуляй в парке!”
5) При условии от 30 до 50 включительно: “Ого, как жарко!”
6) При условии выше 50: “Там такая жара, лучше сиди дома!”
7) В других случаях: “Ошибка!”'''
temperature=int(input("temperature:"))
if temperature<-30:
    print("Там так холодно, лучше дома сиди!")
elif temperature>=-30 and temperature<0:
    print("Холодновато. Оденься потеплее!")
elif temperature>=0 and temperature<15:
    print("Прохладно. Куртку накинь!")
elif temperature>=15 and temperature<30:
    print("Тепло. Иди погуляй в парке!")
elif temperature>=30 and temperature<50:
    print("Ого, как жарко!")
if temperature >=50:
    print("Там такая жара, лучше сиди дома!")
else:
    print("Ошибка!")
"""ЗАДАЧА №3
Вам дается текст:
Посчитайте количество букв s и t ."""
# text="Advertising companies say advertising is necessary and important. It informs people aboutnew products. Advertising hoardings in the street make our environment colourful. Andadverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colourless.But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money"
# print(text.count("s"))#62шт
# print(text.count("t"))#71шт
# print(62+71)#Общее число букв в тексте 's' и 't' 133шт
# """ДОП ЗАДАЧА:
# Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную
# строку из двух имен, буква за буквой.
# Результат: "AAiddialnea"""#Тут надо AAiddialnea или AAiddialneat?Навсякий сделал 2
# girl="Aidana"
# boy="Adilet"
# names=girl+boy
# print(names)
# name="AidanaAdilet"
#A  i  d  a  n  a  A  d  i  l  e   t
#0  1  2  3  4  5  6  7  8  9  10  11
# a=(name[0])
# b=(name[6])
# c=(name[1])
# d=(name[7])
# e=(name[2])
# f=(name[8])
# g=(name[3])
# h=(name[9])
# i=(name[4])
# j=(name[10])
# k=(name[5])
# l=(name[11])
# print(a+b+c+d+e+f+g+h+i+j+k)
# print(a+b+c+d+e+f+g+h+i+j+k+l)


