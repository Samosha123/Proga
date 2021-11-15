#Zad1
info = {}
info["фио"] = "Самохин Александр Вадимович"
info["дата_рождения"]="02 11 2002"
info ["место_рождения"]="Воронеж"
print(info)

spi=[]
info["хобби"]=spi
spi.append("плавание")
spi.append("программирование")

kort=("собака Чарли", "кот Самоша")
info["животные"]=kort

ekz={}
info["ЕГЭ"]=ekz
ekz["Русский"]=80
ekz["Математика"]=75
ekz["Физика"]=73
ekz["Информатика"]=81
ekz["Биология"]=0
ekz.pop("Биология")

vuz={}
info["вузы"]=vuz
vuz["ВГУИТ"]=220
vuz["ВГТУ"]=230
vuz["ВГУ"]=260

print("Данные:",info)

# Список экзаменов ЕГЭ в алфавитном порядке
exams =sorted(ekz)
print("Предметы:", exams)
# Список вузов в алфавитном порядке
uni = sorted(vuz)
print("Вузы:", uni)


print("\nОтветы на вопросы:")
# Выделить имя из info["фио"]
name = info["фио"].split()[1]
glass=["А", "О", "У", "Е", "И", "Я"]
check=name is glass

print("* мое имя начинается на гласную букву:", check)

month = name = info["дата_рождения"].split()[1]

# Родился зимой или летом? (True/False)
born_in_winter_or_summer = ["12", "1", "2", "6", "7", "8"]
check=month is born_in_winter_or_summer
print("* родился летом или зимой:", check)
# Количество хобби и первое из них
hobbies_count = len(info["хобби"])

print(f'* у меня {hobbies_count} хобби, первое \"{info["хобби"][1]}\"')
# Количество сданных экзаменов
print(f'* после окончания школы сдавал {len(info["ЕГЭ"])} экз."')
# # Сумма баллов по экзаменам
sum_mark = ekz["Русский"]+ekz["Информатика"]+ekz["Математика"]+ekz["Физика"]
print(f'* сумма баллов = {sum_mark}"')
# # Максимальный балл среди сданных
msx =[ ekz["Русский"],ekz["Информатика"],ekz["Математика"],ekz["Физика"]]
max_mark=0
for i in range(len(msx)):
    if msx[i]>max_mark:
        max_mark=msx[i]
        i+=1
    else:
        i+=1
print(f'* макс. балл = {max_mark}')

sum_mark=sum_mark-ekz["Информатика"]
vuz_count=0
vuz_mass=[vuz["ВГУИТ"],vuz["ВГТУ"],vuz["ВГУ"]]
for i in range(len(vuz)):
    if sum_mark>=vuz_mass[i]:
        vuz_count+=1
    i+=1   
print(f'* кол-во вузов в которые прохожу: {vuz_count}')


#Zad2 (1var)
from collections import OrderedDict
dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
dct.move_to_end(1,last=True)
dct.move_to_end(5,last=False)
dct.pop(2)
dct[6]=6
print(dct)

#Zad3
strk="159538259823275"
slov={}
for i in strk:
    if (i in slov):
        slov[i]+=1
    else:
        slov[i]=1
print(slov) 
sorted_slov={}
sorted_keys = sorted(slov, key=slov.get,reverse=True)  
j=0
for i in sorted_keys:
    if j < 3:
        sorted_slov[i] = slov[i]   
        j+=1
    else:
        break
print(sorted_slov) 


