#Lambda функции
# def mult_two(number:int)->int:
#     return number*number
# print(mult_two(10))

# lambda_mult_two=lambda number:number*number
# print(lambda_mult_two(10))

# print((lambda number:number*number)(10))

# def add(num1:int=10, num2:int=10)->int:
#     return num1+num2
# print(add(5))

# lambda_add=lambda num1,num2:num1+num2
# print(lambda_add(30,30))

# print((lambda num1,num2:num1+num2)(30,30))

# numbers=[10,20,30,40,50]
# new_numbers=[]
# def mult_two_list(nums:list)->list:
#     for n in nums:
#         new_numbers.append(n*2)
#     return new_numbers
# print(mult_two_list(numbers))

# numbers=[10,20,30,40,50]
# lambda_new_numbers=list(map(lambda nums:nums*2,numbers))
# print(lambda_new_numbers)

# numbers=[10,20,30,40,50]
# print(list(map(lambda nums:nums*2,numbers)))

# print(list(map(lambda nums:nums*2,[10,20,30,40,50])))

# nums=[1,2,3,4,5,6,7,8,9,10]
# chet=[]
# def chet_numbers(numbers:list)->list:
#     for n in numbers:
#         if n%2==0:
#             chet.append(n)
#     return chet
# print(chet_numbers(nums))

# nums=[1,2,3,4,5,6,7,8,9,10]
# lambda_filter_nums=list(filter(lambda numbers:numbers%2==0,nums))
# print(lambda_filter_nums)

# nums=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda numbers:numbers%2==0,nums)))

# print(list(filter(lambda numbers:numbers%2==0,[1,2,3,4,5,6,7,8,9,10])))

#Функция Args,Kwargs
print("Hello","Geeks","World","Python")
print("Hello world")

def welcome(*name:str):
    print(name)
    for n in name:
        print("Здравствуйте", n)
welcome('kurmanbek',"Anton","Anna","Nurbolot")

def student_mean_point(name:str,*points:int)->str:
    print(name,round(sum(points)/len(points)))#round округляет
student_mean_point("Nurbolot",4,5,6,1,2,3,7,8,9,2,1,1,1,1,2)

def translate(**words):
    print(words)
translate(Apple="Яблоко", Phone="Телефон")

