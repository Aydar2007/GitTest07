#Множества set,frozenset

# emails={"Geeks@edu.kg",'kermanbek@gmail.com00',"nur@gmail.com","Geeks@edu.kg"}
# print(emails)

# st={10,1.0,True,"Hello",(10,20,30),False} нельзя list and set
# print(st)

# strange_app=set("TikTok")
# print(strange_app)

# company={"google","Meta","Netflix"}
# company.add("Geeks")
# print(company)
# company.remove("Meta")
# print(company)
# company.pop()
# print(company)

# nums1=[10,20,30,40,50]
# nums2=[30,40,50,60,70]
# print(set(nums1+nums2))

# frzn_set=frozenset({10,20,30,30,20})
# print(frzn_set)
# frzn_set

# import dis
# # print(dis.dis("{1,2,3,4,5}"))
# print(dis.dis("frozenset({1,2,3,4,5})"))

#Dictionary-словари.
# nums=[40,50,10,20,5]
# print(len(nums))
# student={"name":"Nurbolot","age":18}
# print(len(student))
# print(student["name"])
# print(student["age"])
# student.setdefault("job","Python Developer")
# print(student)
# student.pop("age")
# print(student)
# student.popitem()
# print(student)
# student["name"]="Anton"
# print(student)

# osh={
#     "name":"osh",
#     'year':2023,
#     "population":734000
# }
# print(osh.keys())
# print(osh.values())
# print(osh.items())

# for k,v in osh.items():
#     print(k,v)

contact={"MHCS":112}
while True:
    command=input("1-посмотреть,2-добавить,3-удалить,4-обновить:")
    if command=="1":
        print(contact)
    elif command=="2":
            add_name=input("Имя которого надо добавить:")
            add_number=input("Номер которого надо добавить")
            contact.setdefault(add_name,add_number)
            print("Успешно добавленно")
    elif command=="3":
            delete_name=input("Чей номер удалить?")
            contact.pop(delete_name)
            print("Успешно удален")
    elif command==4:
        update_name=input("Чей контакт обновить:")
        new_number=input("Новый номер")
        contact[update_name]=new_number    
        print("Успешно обнавлено")