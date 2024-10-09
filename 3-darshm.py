# # 1-misol
# """
# a=int(input("a ni kiriting"))
# b=int(input("b ni kiriting"))
# evennum=[]
# for i in range(a,b+1):
#     if i % 2 == 0:
#         evennum.append(i)
#
# print(evennum)
#  """
# #2-misol
# """
# a=int(input("a number:"))
# b=int(input("b number:"))
# evennum=[]
# for i in reversed(range(a,b+1)): #for i in range(b,-a,-1)
#     if i % 2 != 0:
#         evennum.append(i)
# print(evennum)
# """
# # 3-misol
# """
# list1 = ["So'z", "yana so'z", 1, 2, 3, "Bayram"]
# TEXT = []
# OTHER = []
# for item in list1:
#     if type(item) == str:
#         TEXT.append(item)
#     else:
#         OTHER.append(item)
# TEXT.sort()
# print("text:",TEXT,end="\n")
# print("other:",OTHER)
# """
# # 4-misol
# # 1-misol
# """
# a=["hoshim","bek","abdulla","kamol","kim","madi","faruc"]
# a_filtr=filter(lambda name: "b" in name,a)
# print(list(a_filtr))
# """
# # 2-misol
# """
# a=["hoshim","bek","abdulla","kamol","kim","madi","faruc"]
# b_map=map(lambda name:name.upper(),a)
# print(list(b_map))
# """
# # 3-misol
# """
# a=["hoshim","bek","abdulla","kamol","kim","madi","faruc"]
# b_map=list(map(lambda name:name.replace("a","A"),a))
# print(b_map)
# """
# # 4-misol
# """
# friends = ["Samandar", "Behruz", "Begali", "Javlon", "Salmon", "Husan", "Bobur", "Otabek"]
#
# friends.sort(key=lambda name: len(name), reverse=True)
#
# sorted_friends = list(filter(lambda name: "e" in name.lower(), friends))
# mapped_friends = list(map(lambda name: name.replace("B", "b"), friends))
#
# print(sorted_friends)
# print(mapped_friends)
# """
# # 5-misol
# """
# def main(n:int):
#     for i in range(n):
#       sum=sum+i
#
# print(sum)
#
# main(10)"""
#
# # 1-misol
# """
# a=int(input("a ni kiriting"))
# b=int(input("b ni kiriting"))
# evennum=[]
# for i in range(a,b+1):
#     if i % 2 == 0:
#         evennum.append(i)
#
# print(evennum)
#  """
# #2-misol
# """
# a=int(input("a number:"))
# b=int(input("b number:"))
# evennum=[]
# for i in reversed(range(a,b+1)): #for i in range(b,-a,-1)
#     if i % 2 != 0:
#         evennum.append(i)
# print(evennum)
# """
# # 3-misol
# """
# list1 = ["So'z", "yana so'z", 1, 2, 3, "Bayram"]
# TEXT = []
# OTHER = []
# for item in list1:
#     if type(item) == str:
#         TEXT.append(item)
#     else:
#         OTHER.append(item)
# TEXT.sort()
# print("text:",TEXT,end="\n")
# print("other:",OTHER)
# """
# # 4-misol
# """
# list = [1, 2, 33, 5, 6, 7, 7]
# target = int(input("Son kiriting: "))
# for i in range(len(list)):
#     for j in range(i + 1, len(list)):
#         if list[i] + list[j] == target:
#             print(f"list[{i}] + list[{j}] = {target}, index: {i}, {j}")
# """
# # 5-misol
# """
# gap = input("Gap kiriting: ")
# a = gap.split()
# a.sort()
# print(" ".join(a))
# """
# # 6-misol
# """
# son = int(input("Son kiriting: "))
# sum = 0
# for i in range(1, son + 1):
#     qator = "+".join(str(x) for x in range(1, i + 1))
#     sum += i
#     print(f"{qator}={sum}")
# """
# # 7-misol
# """
# gap = input("Gap kiriting: ")
# a = gap.split()
# natija = []
# for i in a:
#     if len(i) % 2 == 1:
#         natija.append(i[::-1])
#     else:
#         natija.append(i)
# print(" ".join(natija))
# """
# # 8-misol
# """
# son = int(input("Son kiriting: "))
# a = bin(son)[2:]
# b = a.count('0')
# print(f"Ikkilik sanoq sistemasidagi nollar soni: {b} \nikkilik: {a}")
# """
# # 9-misol
# """
# def tub(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# son = int(input("Son kiriting: "))
# tubs = []
# nextson = son + 1
# while len(tubs) < 5:
#     if tub(nextson):
#         tubs.append(nextson)
#     nextson += 1
# print(" ".join(map(str, tubs)))
# """
# # 9-misol
# """
# soz = input("so'z kiriting: ")
# harf = input("harf kiriting: ")
# natija = soz.replace(harf, harf.upper())
# print(natija)
# """
# # 10-misol
# """
# n = int(input("n kiriting: "))
# sum = 0
# a = ""
# son = 0
# for i in range(1, n + 1):
#     son = son * 10 + 2
#     sum += son
#     a += str(son)
#     if i != n:
#         a+= "+"
# print(f"{a}={sum}")
# """
# # 11-misol
# """
# t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# boshi = t[3]
# oxiri = t[-4]
# print(boshi, oxiri)
# """
# # 12-misol
# """
# list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# newlist = [t[:-1] + (100,) for t in lst]
# print(newlist)
# """
# # 13-misol
# """
# list = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]
# newlist = [t for t in lst if t]
# print(newlist)
# """
# # 14-misol
# """
# list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# slist = sorted(list, key=lambda x: float(x[1]), reverse=True)
# print(slist)
# """
# # 15-misol
# """
# s = input("String kiriting: ")
# t = tuple(s)
# print(t)
# """
# # 16-misol
# """
# list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# maxl = max(list, key=sum)
# print(maxl)
# """
# # 17-misol
# """
# list = [1, 2, 3, 4]
# s = input("String kiriting: ")
# newlist = [s + str(elem) for elem in s]
# print(newlist)
# """
# # .404
# # 1-misol
# """
# def juft(numbers):
#     sum = 0
#     for number in numbers:
#         if number % 2 == 0:
#             sum += number
#     return sum
# list = [1, 2, 3, 4, 5, 6]
# print(juft(list))
# """
# # 2-misol
# """
# def harflar(m):
#     un = "aeiouAEIOU"
#     sum = 0
#     for harf in m:
#         if harf in un:
#             sum += 1
#     return sum
# satr = str(input("biror so'z kiriting: "))
# print(harflar(satr))
# """
# # 3-misol
# """
# def tuple(tupl):
#     max = tupl[0]
#     for i in tupl:
#         if i > max:
#             max = i
#     return max
# a = (3, 5, 2, 9, 1)
# print(tuple(a))
# """
# # 4-misol
# """
# def sum(set1, set2):
#     return set1.intersection(set2)
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(sum(set1, set2))
# """
# # 5-misol
# """
# def dicti(d):
#     dic = {}
#     for key, value in d.items():
#         dic[value] = key
#     return dic
# d = {1: "a", 2: "b", 3: "c"}
# print(dicti(d))
# """
# # vvfbf
# """
# from utils.unit2.getter2 import dicti
#
# d = {1: "a", 2: "b", 3: "c"}
# try:
#     d= {3:"b"}
# except IndexError  as exs:
#     print("IndexError")
# except Exception :
#     print("xato")
# else:
#     print(dicti(d))
# finally:
#     print("pox")
# """
# # jon fayllar06
# # 1-misol fayl ochish va uni ichiga yozish
# """
# a="salom fayl"
# with open('bir.txt','w') as file:
#     file.write(f"hello {a}\n""yana salom" )
# print("tugadi")
# """
# import json
#
# # 2-misol fayldagi ma'lumotni o'qish
# """
# with open('bir.txt','r')as file:
#     a=file.read()
# print(a)
# """
# # 3-misol fayl qatorlari
# """
# i=1
# with open('bir.txt','r')as file:
#     for line in file:
#         print(f"{i}.",line.strip())
#         i+=1
# """
# # 4-misol fayl qatorlarini sanash
# """
# with open('bir.txt','r')as file:
#     for index,line in enumerate(file):
#         print(f"{index+1}.",line.strip())
# """
# # 5-misol fayl ichida kursorni harakatlantrish
# """
# with open('bir.txt','r')as file:
#     file.seek(5)
#     content=file.read(6)     #-6
#     print(file.tell())
# print(content)
# """
# # 6-misol json fayllarni ichiga ma'lumot yozish
# """
# import json
#
# data={
#     "name":"bekzod",
#     "age":23,
#     "city":"Andijan"
# }
# with open('data.json','w')as file:
#     json.dump(data,file,indent=4)
# """
# # 7-misol json fayllarni o'qish
# """
# import json
#
# with open("data.json",'r')as file:
#     data=json.load(file)
# print(data["age"])
# with open('data.json','r')as file:
#     data= file.read()
# print(data)
# """
# # 8-misol matn o'zgaruvchini stringdan jsonga o'tadi
# """
# import json
# json_string='{"name":"Bekzod","age":23,"city":"Andijan"}'
#
# data= json.loads(json_string)
# print(f"Name:{data['name']}")
# print(f"Age:{data['age']}")
# print(f"City:{data['city']}")
# print(data)
# """
# # 9-misol json faylni stringga aylantrib terminalgda chiqarish
# """
# import json
#
# json_data='''
# {
#   "name":"Bekzod",
#     "detal":{
#         "age":23,
#         "address":{
#             "street":"25 obrat",
#             "city": "andikon",
#             "state": "uzpakistan"
#         },
#         "contact":["bek@gmail.com","99894-598-79-05"]
#     }
# }'''
# data=json.loads(json_data)
# name=data['name']
# age=data['detal']['age']
# city=data['detal']['address']['state']
# email=data['detal']['contact'][1]
# print(f"Name:{name}")
# print(f"Age:{age}")
# print(f"City:{city}")
# print(f"Number:{email}")
# """
# # 10-misol stringdan faylga yuborib uni oqitish
# """import json
# json_string='{"name":"Bekzod","age":23,"city":"Andijan"}'
# with open('new.json','w')as file:
#     json.dump(json.loads(json_string),file,indent=4)
# with open('new.json','r')as file:
#     data=json.load(file)
# print(data['city'])
# """
# # qo'shimcha 1-misol
# """
# with open('new.json','r')as file:
#     data=json.load(file)
# print(data['age'])
# """
# # qo'shimcha 2-misol
# '''with open('new.json','r')as file:
#    data= json.load(file)
# print(data)
# js='{"email":"bekzod@gmail.com"}'
# with open('new.json','w')as file:
#     json.dump(json.loads(js),file,indent=4)
# with open('new.json','r')as file:
#    data= json.load(file)
# print(data)
# '''
# # qo'shimcha dars 3-misol faylga ma'lumot qo'shish
# '''import json
# json_string='{"name":"Bekzod","age":23,"city":"Andijan"}'
# with open('new.json','w')as file:
#     json.dump(json.loads(json_string),file,indent=4)
# with open('new.json','r')as file:
#     data=json.load(file)
# print(data['name'])
# js='{"name":"Bekzod","age":23,"city":"Andijan","email":"bekzod@gmail.com"}'
# with open('new.json','w')as file:
#     json.dump(json.loads(js),file,indent=4)
# with open('new.json','r')as file:
#    data= json.load(file)
# print(data['email'])
# '''
# # 405 vazifasi
# # 1-misol
# """
# try:
#     a = float(input("1-sonni kiriting: "))
#     b = float(input("2-sonni kiriting: "))
#     natija = a / b
#     print(f"{a} / {b} natija: {natija}")
# except ZeroDivisionError:
#     print("Xato: 2-son 0 bo'lamaydi!")
# except Exception:
#     print("Xato: Iltimos, raqam kiritishingizni tekshiring.")
# """
# # 2-misol
# """
# from utils.get import orta
# def main():
#     try:
#         sonlar = list(map(float, input("Sonlarni kiriting with ',': ").split(',')))
#         o = orta(sonlar)
#         print(f"O'rtacha qiymat: {o}")
#     except ValueError as e:
#         print(f"Xato: {e}")
# if __name__ == "__main__":
#     main()
#
# """
# # 406-vazifasi
# # 1-misol
# # import json
# #
# # dataes = [{"Name": "John", "Age": 15},{"Name": "Alice", "Age": 14}]
# # with open('data.json', 'w') as f:
# #     json.dump(dataes, f, indent=4)
# #
# # with open('data.json', 'r') as f:
# #     data = json.load(f)
# #     for i in data:
# #         print(f"Name:{i['Name']} Age:{i['Age']} ")
#
#
# #2-misol
# # import json
# #
# # dataes = {"Name": "Tom", "Age": 13}
# #
# # with open('students.json', 'w') as f:
# #     json.dump([dataes], f)
# #
# # var1 = {"Name": "Som", "Age": 23}
# # with open('data.json', 'a') as nf:
# #     nf.write(f"{var1}")
# #
# # with open('students.json', 'r') as nf:
# #     data = json.load(nf)
# #     for i in data:
# #         print(f"Name: {i['Name']}, Age: {i['Age']}")
#
# #3-misol
# # lines = ["Finish homework", "Clean the room", "Read a book"]
# # with open('lines.txt', 'w') as f:
# #     count = 1
# #     for line in lines:
# #         f.write(f"{count}. {line}\n" )
# #         count += 1
# #
# # with open('lines.txt', 'r') as f:
# #     print(f.read())
#
# #4-misol
# # with open('books.txt', 'w') as f:
# #     f.write("Harry Potter, J.K. Rowling\n")
# #     f.write("The Hobbit, J.R.R. Tolkien\n")
# #     f.write("Pride and Prejudice, Jane Austen")
# #
# #
# # def kitoblar():
# #     with open('books.txt', 'r') as f:
# #         kitob = f.readlines()
# #
# #     nom = input("Kitob nomini kiriting: ")
# #
# #     found = False
# #     for book in kitob:
# #         ismi, mualif = book.strip().split(', ')
# #         if ismi.lower() == nom.lower():
# #             print(f"Kitob: {ismi}, Muallif: {mualif}")
# #             found = True
# #             break
# #
# #     if not found:
# #         print("Kitob topilmadi.")
# #
# #
# # kitoblar()
#
# #5-misol
#
# import json
#
# def dataes(student):
#     with open(student, 'r') as f:
#         return json.load(f)
#
# def func1(datan):
#     students = datan['students']
#     for student in students:
#         ism = student['name']
#         baho = student['grades']
#         urtacha = sum(baho) / len(baho)
#         print(f"Name: {ism}, Average Grade: {urtacha:.2f}")
#
#
# if __name__ == "__main__":
#     fayl = 'grades.json'
#     data = dataes(fayl)
#
#     func1(data)
#
#
#
#
#
#
#
# 1-misol
"""import json

data = [{"Name": "Bekzod", "Age": 23},{"Name": "gulchapchap", "Age": 18}]
with open('hmw.json', 'w') as f:
    json.dump(data, f, indent=4)

with open('hmw.json', 'r') as f:
    data = json.load(f)
    for i in data:
        print(f"Name:{i['Name']} Age:{i['Age']} ")
"""
# 2-misol
"""import json

data = {"Name": "Tom", "Age": 13}
with open('students.json', 'w') as f:
    json.dump([data], f)
variable = {"Name": "Bekzod", "Age": 23}
with open('data.json', 'a') as nf:
   nf.write(f"{variable}")
with open('students.json', 'r') as nf:
    data = json.load(nf)
    for i in data:
     print(f"Name: {i['Name']}, Age: {i['Age']}")
"""
# 3-misol
"""
lines = ["uyga vazifa bajaridi!", "xona tozalandi", "kitob o'qildi"]
with open('line.txt', 'w') as f:
    count = 1
    for line in lines:
        f.write(f"{count}. {line}\n" )
        count += 1

with open('line.txt', 'r') as f:
    print(f.read())
"""
# 4-misol
#
# with open('books.txt', 'w') as file:
#     file.write("Sariq devni minib, X.To'xtaboyev\n")
#     file.write("Atom odatlar, clewrem\n")
#     file.write("Puaro, Anna Austen")
# def kitoblar():
#     with open('books.txt', 'r') as file:
#         kitob = file.readlines()
#     nom = input("Kitobni nomini kiriting: ")
#     found = False
#     for book in kitob:
#         ismi, mualif = book.strip().split(', ')
#         if ismi.lower() == nom.lower():
#             print(f"Kitob: {ismi}, Muallifi: {mualif}")
#             found = True
#             break
#     if not found:
#         print("Kitob yo'q!")
# kitoblar()
# 5-misol

# import json
#
# def oquvchi _malumotlarini_ol(fayl_nomi):
#     with open('grades.json', 'r') as f:
#         return json.load(f)
#
# def oquvchi_baholarini_chop_et(datan):
#     students = datan['students']
#     for student in students:
#         ism = student['name']
#         baho = student['grades']
#         urtacha = sum(baho) / len(baho)
#         print(f"Name: {ism}, Average Grade: {urtacha:.2f}")
#
# if __name__ == "__main__":
#     fayl_nomi = 'grades.json'
#     datan = oquvchi_malumotlarini_ol(fayl_nomi)
#     oquvchi_baholarini_chop_et(datan)
# fayl
