#Цыклы for,while
# print(1)
# print(2)
# print(3)

# for i in range(1,1000,2):
#     print(i)

# cars=["BMW",'TOYOTA',"Mercedes","HONDA"]
# print(cars)
# for car in cars:
#    if "Mercedes"==car:
#       print(True)
#    else:
#       print(False)

# numbers=[10,1,3,5,2,6,5,45,99,42,15,65,32,12,546]
# # print(numbers)
# for number in numbers:
# #    print(number)
#    if number %2==0:
#       print(number,"Четный")
#    else:
#         print(number,"Нечетное")
# nums=[]
# for i in range(1,101):
#     nums.append(i)
#     if i==70:
#         print("STOP")
#         # break остонавливает
#         continue#продолжает
# print(nums)
# it="GEEKS PYTHON"
# for i in it:
#     print(i)

# tup=(101,400.6,True,"Hello",[10,20,30])
# for t in tup:
#     print(t)

# num="1001"# в int нельзя bolling and float
# for n in num: 
#     print(n)

# import random
# # print(random.randint(1,10))
# # names=["Nurbolot","Askhat","Nurtilek","Anton"]
# # print(type(random.choice(names)))

# password_generator="qwertyuiopasdfghjklzxcvbnm1234567890"
# How_many_password=int(input("Сколько паролей вам нужно:"))
# len_password =int(input("Длина паролей:"))
# for j in range(How_many_password):
#     res=""
#     for i in range(len_password):
#         choice=random.choice(password_generator)
#         res=res+choice
#     print(res)

# num1=10
# num2=20
# while num1<num2:
#     num1=num1+1
#     print(num1)
# n=0
# while True:
#     n=n+1
#     print(n,"Geeks")
#     if n ==1000000:
#         print("STOP")
#         break
# import random
# password=1111
# print(password)
# n=1111
# while True:
#     print(n)
#     if password==n:
#         print(n,"is password")
#         break
#     n=n+1
# for i in range(10,100,2):
#     print(i)

# start=10
# end=100
# step=10
# while True:
#     print(start)
#     start=start+step
#     if start==end:
#         break
import requests
res=requests.get("https://kyzmat24.com/api/users").json()
for r in res:
    # print(r['username'])
    if r['username']=="kuba":
        print("Он есть")
        break
