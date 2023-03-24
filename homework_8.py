"""1) Напишите функцию, которая принимает список, из списка выдает случайное
значение из списка и записывает результат в txt файл. Список language =
["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]"""
language =["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
from random import choice
choice_language=choice(language)
with open("language1.txt","w") as e:
    e.write(choice_language)


language =["Python", "Java", "Kotlin", "JavaScript", "C#","RUBY"]
from random import choice
choice_language=choice(language)
e=open("languege2.txt","w")
e.write(choice_language)
e.close()
"""2) У нас есть переменная text которая, хранит в себе текст:
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum
has been the industry's standard dummy text ever since the 1500s, when an unknown
printer took a galley of type and scrambled it to make a type specimen book. It has
survived not only five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularized in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing
software like Aldus PageMaker including versions of Lorem Ipsum.
Откройте файл text.txt и запишите текст в файл 2 способами"""
text=("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularized in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
with open("text1.txt","w") as f:
    f.write(text)
f=open("text1.txt","a")
f.write('\n'+text)
f.close()
"""ДОП ЗАДАЧА:
3) Написать программу, которая откроет созданный в задаче 2 файл text.txt,
скопирует весь текст и запишет его в новый файл wikipedia.txt """
with open("text1.txt","r") as r:
    p=r.read()
with open("wikipedia.txt","w") as g:
    g.write(p)
