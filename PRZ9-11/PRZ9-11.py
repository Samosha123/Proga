# #Zad1
# #1.1
def z1_1(x):
    if x >=0:
        f= x**(1/2)+x**2
    else:
        f = 1/x
    return f
# #1.2
def z1_2 (a,b):
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a
    return max,min
# #1.3
def z1_3(m_birth,y_birth):
    m_today = 11
    y_today = 2021
    y_count = y_today - y_birth
    if m_today > m_birth:
        y_count-=1
    return y_count
# #1.4
def z1_4 (x1_4,y1_4):
    if x1_4 < 0 and y1_4 <0:
        q_num = 3
    elif x1_4 < 0 and y1_4 >0: 
        q_num = 2
    elif x1_4 > 0 and y1_4 > 0:
        q_num = 1
    else:
        q_num = 4
    return q_num

# #Zad2
# #2.1
def z2_1(num_list):
    num_sum = 0

    for num in num_list:
        num_sum += num
    num_length = len(num_list)

    return num_sum, num_length
# #2.2
def z2_2(x):
    a = 0
    while x >= a:
        print(a)
        a+=5
# #2.3
def z2_3 (a):
    sum = 0.0
    n = 0
    while sum <= a:
        n += 1
        sum += 1/n
    return (n)
# #2.4
def z2_4 (x):
    sum = 0
    count = 0
    while x % 10 != 0:
        sum = sum + x % 10
        x = int(x / 10)
        count+=1
    return sum,count
# #2.5
def z2_5(k, s, start):
    res_num= []
    count = 0

    for i in range(start, 1000):
        if int(str(i)[-1]) == k and i % s == 0:
            res_num.append(i)
            count+=1
        if count == 10:
            break
    return res_num
#Zad3
#3.1    
def z3_1(numbers_list):
    for number in sorted(numbers_list):
        print(number, end=" ")
    print()
    for number in sorted(numbers_list, reverse=True):
        print(number)

#3.2
def z3_2(a,b):
    ran = b - a
    sum = 0
    proz = 1
    arif = 0
    geom = 0
    for i in range (a,b+1):
        sum+=i
        proz*=i
        arif = sum / (ran + 1)
        geom = proz**(ran + 1)
    return sum, proz,arif, geom
#3.3
def z3_3(s,p):
    p = p / 100
    sum = 0
    temp = 0
    for i in range (2,10):
        temp = s * p
        s+=temp
        sum+= s
        print("За", i , "день лыжник преодолел: ", s)
    print("Суммарная дистаниця: ")
    return sum
#3.4
def z3_4(p):
    mass_gruz = [2,5,1,10,9]
    sum = 0
    for i in range (0,len(mass_gruz)):
        sum+= mass_gruz[i]
    if sum<=p:
        print("Перевозка возможна")
    else:
        print("Перевозка не возможна")
    
#Zad4
#4.1
def z4_1():
    n = 0
    sum_n = 0
    count = 0
    while True:
        a = int(input())
        if a == 0:
            break
        else:
            sum_n += a
            count += 1
    return sum_n,count
#4.2
def z4_2(stroke):
    vowels_num = 0
    consonants_num = 0
    current_stroke = stroke.lower()

    for symbol in current_stroke:
        if symbol in "ауоиэыяюеё":
            vowels_num += 1
        elif symbol in "бвгджзйклмнпрстфхцчшщ":
            consonants_num += 1
        else:
            continue

    return vowels_num, consonants_num
#Zad5
#5.1
def z5_1(a,b,c):
    mass = []
    for i in range (a,b):
        if i%c==0:
            mass.append(i)
    return mass
#5.2
import math
def z5_2(n):
    mass = []
    for i in range (100,999):
        countNum = len(str(i)) - 1
        divider = 10**countNum
        for g in range(0,countNum + 1):
            temp = math.floor(i / divider)
            mass.append(temp % 10)
            divider /= 10
        sum = 0
        for j in mass:
            sum = sum + j
        if sum == n:
            print(mass)
        mass.clear()
#5.3
def z5_3():
    klass = [-184,175,191,-194,-181,180,-199,150,-178,-190,178] 
    sum_m = sum_f = count_m = count_f = 0
    for i in klass:
        if i < 0:
            i = i*(-1)
            sum_m+=i
            count_m+=1
        else:
            sum_f+=i
            count_f+=1
    sr_m= sum_m/count_m
    sr_f = sum_f / count_f
    return round(sr_m,1), round(sr_f,1)
#5.5    
def z5_5(n):
    for number_1 in range(1, n+1):
        for number_2 in range(1, n+1):
            print(number_1, "x", number_2, "=", number_1 * number_2, end="\t")
        print("\n")
#5.6
def z5_6(n):
    result_col = 0
    for i in range(1, int(n) + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                result_col += 1
        print(i, result_col * "*")
        result_col = 0
#5.7
def z5_7(n):
    result_numbers = []

    for number_1 in range(2, n + 1):
        for number_2 in range(2, number_1):
            if number_1 % number_2 == 0:
                break
        else:
            result_numbers.append(number_1)

    return result_numbers
#Zad6
#6.1
def z6_1(numbers):
    plus_list = [number for number in numbers if number >= 0]
    neg_list = []
    sr_arifm = 0
    sr_geom = 1

    for number in numbers:
        if number < 0:
            neg_list.append(number)

    for number in plus_list:
        sr_arifm += number
    for number in neg_list:
        sr_geom *= number

    sr_arifm /= len(plus_list)
    sr_geom **= 1 / len(neg_list)

    print("Исходный список:", numbers)
    print("Список положительных чисел:", plus_list)
    print("Список отрицательных чисел:", neg_list)
    print("Среднее арифметическое списка положительных чисел:", sr_arifm)
    print("Среднее геометрическое списка отрицательных чисел:", sr_geom)
#6.2
def z6_2(numbers):
    all_pos = True
    one_null = False
    all_chet = True
    one_nechet = False

    for number in numbers:
        if number <= 0:
            all_pos = False
        if number == 0:
            one_null = True
        if number % 2 != 0:
            all_chet = False
            one_nechet = True

    if any(number <= 0 for number in numbers):
        all_pos = False
    if any(number == 0 for number in numbers):
        one_null = True
    if any(number % 2 != 0 for number in numbers):
        all_chet = False
        one_nechet = True

    return all_pos, one_null, all_chet, one_nechet
#6.3
def z6_3(stroke, symbol):
    stroke_list = stroke.split()

    for i in range(0, len(stroke_list)-1):
        if symbol in stroke_list[i]:
            stroke_list.pop(i)

    result_stroke = " ".join(stroke_list)
    print(result_stroke)
#6.4
def z6_4(rows, row_num, col_num):
    sum_free_places = 0

    for row in range(0, len(rows)):
        for col in rows[row]:
            if col == 0:
                sum_free_places += 1

    print("На данный момент в зале свободно:", sum_free_places, "мест(а)")

    if rows[row_num-1][col_num-1] == 0:
        print("Место " + str(row_num) + "." + str(col_num) + ": свободно")
    else:
        print("Место " + str(row_num) + "." + str(col_num) + ": занято")
#6.5
def z6_5(peoples, symbol):
    def sort_key(e):
        return e[4]

    mans = []
    mans_symbol = 0
    girls = []
    girls_symbol = 0

    sorted_peoples = sorted(peoples, key=sort_key)
    print("Самый молодой сотрудник:", sorted_peoples[0][0], sorted_peoples[0][1], sorted_peoples[0][2])
    print("Самый старый сотрудник:", sorted_peoples[-1][0], sorted_peoples[-1][1], sorted_peoples[-1][2])

    for people in peoples:
        if people[3] == "М":
            mans.append(people)
        else:
            girls.append(people)

    for man in mans:
        if man[1][0].lower() == symbol:
            mans_symbol += 1

    for girl in girls:
        if girl[1][0].lower() == symbol:
            girls_symbol += 1

    cond_result = "\" в женском коллективе" if girls_symbol > mans_symbol else "\" в мужском коллективе"
    print("Большее количество людей, у которых имя начинается на букву \"" + symbol + cond_result)
#6.6
def z6_6(banks):
    min_sum = banks[0]["initial_sum"]
    min_sum_bank = banks[0]

    max_benefit = banks[0]["initial_sum"] * banks[0]["rate"] / 100
    max_benefit_bank = banks[0]

    for bank in banks:
        if bank["initial_sum"] < min_sum:
            min_sum = bank["initial_sum"]
            min_sum_bank = bank
        if bank["initial_sum"] * bank["rate"] / 100 > max_benefit:
            max_benefit = bank["initial_sum"] * bank["rate"] / 100
            max_benefit_bank = bank

    print("Самым доступным банком является банк:", min_sum_bank["name"])
    print("Самым выгодным банком является банк:", max_benefit_bank["name"])

print("№1.1")
print(z1_1(4))

print("№1.2")
print(z1_2(31,15))

print("№1.3")
print("Введите день рождения: ")
m_birth = int (input())
print("Введите год рождения: ")
y_birth = int (input())
print("Возраст человека: ", z1_3(m_birth,y_birth))

print("#1.4")
print("Введите координаты x и y: ")
x1_4 = int(input())
y1_4 = int(input())
print("Номер координатной четверти: ", z1_4(x1_4, y1_4))

print("№2.1")
numbers_2_1 = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
result_2_1 = z2_1(numbers_2_1)
print("Сумма чисел:", result_2_1[0], "| Количество введенных чисел:", result_2_1[1])

print("№2.2")
print("Последовательность чисел кратных 5: ")
print(z2_2(61))

print("№2.3")
print("Введите вещественное число:")
a = float(input())
print("Наименьшее натууральное n: ")
print(z2_3(a))

print("№2.4")
print("Введите натуральное чилсло: ")
x = int(input())
print("Сумма и количесвто чисел: ",z2_4(x))

print("№2.5")
print(z2_5(4,2,6))

print("№3.2")
print("Введите числа a и b: ")
a = int(input())
b = int(input())
print(z3_2(a,b))

print("№3.3")
print(z3_3(2,50))

print("№3.4")
print(z3_4(10))

print("№4.1")
print("Введите список (0 - последнее число)")
print(z4_1())


print("№5.1")
a = int(input())
b = int(input())
print(z5_1(a,b,2))

print("№5.2")
print(z5_2(15))

print("№5.3")
sr_m, sr_f = z5_3()
print(f'Средний рост мальчиков {sr_m}, срединий рост девочек {sr_f}')

print("№5.5")
print(z5_5(5))

print("№5.6")
number_5_6 = int(input("Введите число до которого будет произведен перебор: "))
z5_6(number_5_6)

print("№5.7")
number_5_7 = int(input("Введите число до которого будет произведен перебор: "))
result_numbers_5_7 = z5_7(number_5_7)
print("Результат: ", end="")
for number in result_numbers_5_7:
    print(number, end=" ")

print("№6.1")
numbers_6_1 = list(map(float, input("Введите список чисел через пробел: ").split()))
z6_1(numbers_6_1)

print("№6.2")
numbers_6_2 = list(map(int, input("Введите список чисел через пробел: ").split()))
result_6_2 = z6_2(numbers_6_2)
print("Все элементы списка положительные числа" if result_6_2[0] else "Не все элементы списка положительные числа")
print("В списке есть хотя бы один нулевой элемент" if result_6_2[1] else "В списке нет ни одного нулевого элемента")
print("Все элементы списка четные числа" if result_6_2[0] else "Не все элементы списка четные числа")
print("В списке есть хотя бы один нечетный элемент" if result_6_2[0] else "В списке нет ни одного нечетного элемента")

print("№6.3")
stroke_6_3 = input("Введите исходное предложение: ")
symbol_6_3 = input("Введите букву, которую необходимо удалить из всего предложения: ")
z6_3(stroke_6_3, symbol_6_3)

print("№6.4")
print("-- Разработчик --")
range_size_6_4 = int(input("Введите количество рядов в кинотеатре: "))
rows_6_4 = []

for i in range(0, range_size_6_4):
    rows_6_4.append(list(map(int, input("Ряд " + str(i+1) + ": ").split())))

print("-- Пользователь --")
row_num_6_4 = int(input("Введите номер ряда: "))
col_num_6_4 = int(input("Введите номер места в ряду: "))

print("№6.5")

range_size_6_5 = int(input("Введите количество сотрудников: "))
peoples_6_5 = []

for i in range(0, range_size_6_5):
    peoples_6_5.append(list(map(str, input("Сотрудник: ").split())))
    peoples_6_5[i][4] = int(peoples_6_5[i][4])

symbol_6_5 = input("Введите первую букву имени для сравнения: ")

z6_5(peoples_6_5, symbol_6_5)

print("---------- Задание 6.6 ----------")

range_size_6_6 = int(input("Введите количество банков: "))
banks_list_6_6 = []
banks_list_dicts_6_6 = []

for i in range(0, range_size_6_6):
    banks_list_6_6.append(list(map(str, input("Банк: ").split())))
    banks_list_dicts_6_6.append({"name": banks_list_6_6[i][0], "initial_sum": int(banks_list_6_6[i][1]), "rate": float(banks_list_6_6[i][2])})

z6_6(banks_list_dicts_6_6)