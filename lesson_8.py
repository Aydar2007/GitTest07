#Модули
# import moduls
# print(moduls.add(20,30))
# print(moduls.hello())
# print(moduls.lambda_add(20,30))
# print(moduls.it)

# from moduls import add,hello
# print(add(30,40))
# print(hello())

# from moduls import*
# print(add(20,60))

# from main import choice_names
# from moduls import lst_names
# print(choice_names(lst_names))

#Работа с файлами
# f=open("python.txt",'w')
# f.write("Geeks Python")
# f.close()

# r=open("python.txt")
# print(r.read())
# r.close()
py=open('hello.py',"w")
py.write("print('Hello World')")
py.close

# py_r=open('lesson_8.py')
# print(py_r.read())
# py_r.close()
# write_py=open('lesson_8.py','a+')
# write_py.write("""
# py_r=open('lesson_8.py')
# print(py_r.read())
# py_r.close()
# """)
# write_py.close()
# py_r=open('lesson_8.py')
# print(py_r.read())
# py_r.close()

# n=0
# while True:
#     n+=1
#     f=open(f'hello{n}.py','w')
#     f.write(f"print('Hello{n}')")
#     f.close()
#     if n==100:
#         break
# import os
# n=0
# while True:
#     n+=1
#     os.remove(f'hello{n}.py')
#     if n==100:
#         break

# with open ("geeks.py","w") as f:
#     f.write('it="Geeks"')

# with open('geeks.py') as r:
#     print(r.read())



while True:
    command=input('1-добавляет,2-посмотреть,3-удалить:')
    if command=="1":
        add_name=input("напишите имя:")
        add_number=input("Напишите номеh:")
        with open("contacts.txt","w") as contacts:
            contacts.write(f"{add_name},{add_number}\n")
        print("Успешно записано")
    elif command=="2":
        with open("contacts.txt") as read_contacts:
            print(read_contacts.read())
    elif command=="3":
        delete_name=("Чей контакт удалить:")       
print("Geeks Hello")
        
