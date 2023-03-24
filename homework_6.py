"""1Напишите функцию, которая принимает фразу, и возвращает его сокращенную
форму.
Например: Кыргызская Республика -- КР. Ruby on Rails -- ROR. For your interest --
FYI и т.п."""
def short_word(word:str)->str:
    split_word=word.split()
    res=""
    for i in split_word:
        res += i[0].upper()
    return res
print(short_word("Кыргызская Республика"))
"""2) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной
фразе было использовано. Например: “Money, money, money, it’s always sunny, in
the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1,
# world: 1."""
def count_words(word:str):
    word_split=word.lower().replace(',','').split()
    res={}
    for n in word_split:
        # print(word_split.count(n))
        res[n]=word_split.count(n)
    return res
print(count_words("Money,money,money, It's always sunny, in the richmen's world"))
"""3) Напишите функцию, которая принимает слово и возвращает True, если слово
изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False"""
def d(word:str):
    word_dict=list(word)
    double=set(word_dict)
    if len(word_dict)==len(double):
        return True
    return False
print(d("dr doctor"))
"""4) Напишите функцию где мы передаем через аргументы число n как целое
integer, надо вывести целое число в перевернутом виде
например: n = 27, тогда перевёрнутое n это 72
"""
def reverse_int(num:int=23)->int:
    return int(str(num)[::-1])
print(reverse_int(231))    
"""ДОП ЗАДАНИЕ:
5) Напишите функцию -- чат-бот с бесконечным циклом, который
a. Всегда отвечает “Конечно!” на любой вопрос
b. Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
c. Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же
духе!” Если вызвал функцию, но ничего не передал.
d. В любых других случаях, отвечает “ну и что”"""
while True:
    a=input("Приветсвует чат-бот,задайте свой вопрос:")
    if "Вот так" in a:
        print("Успокойся")
    elif a==(""):
        print("Как классно, когда ты молчишь. Продолжай в том же духе!")
    else:
        print("Конечно!")