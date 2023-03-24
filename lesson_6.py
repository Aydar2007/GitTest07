#Functions-Функции
# def Calc():#Лучше называть с маленькой буквы
#     num1=int(input("Первое число:"))
#     num2=int(input("Второе число:"))
#     print(num1+num2)
# def add(num1,num2):
#     print(num1+num2)
# add(10,40)#Вызываем функцию add и получаем
# def welcome():
#     name=input("Ваше имя:")
#     print(name,"Здравствуйте")
# welcome()

# def chet_nechet(lst:list)->str:
#     for nums in lst:
#         if nums%2==0:
#             print(nums,"четное")
#         else:
#             print(nums,"Не четное")
# numbers=[1,3,10,1001,400,403,102,101,607,808,888,678,109]
# chet_nechet(numbers)
# # chet_nechet((20,30,50))
# def add(num1:int, num2:int)->int:
#     print(num1+num2)

# def sub(num1:int, num2:int)->int:
#         print(num1-num2)

# def mult(num1:int, num2:int)->int:
#         print(num1*num2)

# def div(num1:int, num2:int)->float:
#         print(num1/num2)
# def main(numbers1:int,numbers2:int,operator:str)->int:
#     if operator =="+":
#         add()
#     if operator =="-":
#         sub()
#     if operator =="+":
#         mult()
#     if operator =="+":
#         div()
#     else:
#         print("Такого оператора не сушествует")
# main(10,40,"-")
# def get_name(name:str="Defolt"):
#     """Hello Geeks Students"""
#     print(name)
# get_name()
# def add(num1:int=1, num2:int=1)->int:
#     return num1+num2#можно и (num1+num2)
# print(add(20+19))
# def hello():
#     while True:
#         print("Hello")
#         return"Hello"
# hello()

try:
    num1=int(input("Первое число:"))
    num2=int(input("Второе число:"))
    print(num1/num2)
except BaseException:
    if num2==0:
        print("Числа на ноль не делятся")