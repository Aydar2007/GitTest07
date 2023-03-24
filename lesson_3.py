#List-спискиdis
# name1="Nurbolpt"
# name2="Anton"
# name3="Bayzak"
# name4="Adilet"

# names=["Nurbolot","Anton","Bayzak","Adilet"]
# print(names)

# lst=[10,1.0,"Geeks",False]
# print(lst[2][0])
# print(lst[0:2][1])

# number=10
# number=11
# cities=["bishkek","osh","naryn","talas"]
# print(cities)
# cities.append("Batken") #Метод append добавляет элемент в конец списка
# print(cities)
# cities.append("Tokmok") #Метод append добавляет элемент в конец списка
# print(cities)
# cities.insert(2,"Karakol")# Метод insert добавляет по индексу и переставляет 
# print(cities)
# cities.remove("Tokmok")#Метод remove удаляет элемент по значению ,кооторую мы передаем
# print(cities)
# cities.pop(0)#метод pop удаляет элемент по индексу
# print(cities)
# del cities[0:2]#Оператор del удаляет из списка по индексу и также по срезам
# print(cities)
# cars=["Toyota","Honda","Mersedes","Honda","BMW","1","10"]
# print(cars.count("Honda"))
# print(cars.index("Toyota"))
# cars[0]='Kia'
# print(cars[1:4:2])

# print (cars[::-2])
# cars.sort()
# print(cars)

# numbers=[10,11,13,51,45,5412,4941,1244]
# # numbers.sort(reverse=True)
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# if 100 in numbers:
#     print(True)
#  else:
#     print(False)
# numbers.clear()
# print(numbers)
# nums1=(10,20,30,40,50)
# nums2=(60,70,80,90,100)
# num3=nums1+nums2
# print(num3)
# num3.sort(reverse=True)
# print(num3)

# numbers=[2.0,10,"Hello",True,[10,20,30]]
# print(numbers)
# tuple-кортежи
# tup=(10,3.0,"Geeks",False)
# print(tup)
# print(tup.count(10))
# print(tup.index("Geeks"))
# print(tup[2])
# print(tup[0:2])
# lst_tup=list(tup)
# print(lst_tup)
# lst_tup.append([1,2,3,4])
# print(lst_tup)
# tup=tuple(lst_tup)
# print=tup

# import dis

# dis.dis("[1,2,3,4]")
# dis.dis("(1,2,3,4)")
tup=(10,)
print(type(tup))