#Первое задание
int(673.3123)#строка 673.3123 из float превратится в integer
float(512)#строка 512 из integer превратится в float
int(float(str(192))) 
"""строка 192 из integer превратится в string, из string превратилось в float, из float превратилось в integer"""
float(173)+5#строка(173)+5 из integer превратится в float будет 173.0+5
str(193.000000000001)#строка 193,000000000001 из float превратится в string
#Второе задание
#Это Обьеденение двух или более строк в одну
a=("Calling ")
b=(str(911))
c=a+b
print(c)
a=('abc')
b=('xyz')
c=a+b
print(c)
#Третье задание
a=589
b=932.901
c="Hello world"
d="892.01"
"""Можно складывать a+b=1521.9009999999998,
c+d='Hello world892.01'"""
y=(str(a))   
r=(str(b))
v=(589+892.01)
print(c+y,d,r+y,v)
