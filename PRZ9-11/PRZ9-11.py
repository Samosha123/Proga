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
def z2_1():
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
    return (sum_n,count)
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
    return
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

# print("№1.1")
# print(z1_1(4))

# print("№1.2")
# print(z1_2(31,15))

# print("№1.3")
# print("Введите день рождения: ")
# m_birth = int (input())
# print("Введите год рождения: ")
# y_birth = int (input())
# print("Возраст человека: ", z1_3(m_birth,y_birth))

# print("#1.4")
# print("Введите координаты x и y: ")
# x1_4 = int(input())
# y1_4 = int(input())
# print("Номер координатной четверти: ", z1_4(x1_4, y1_4))

# print("№2.1")
# print("Че то он мне не то выводит")
# print(z2_1())

# print("№2.2")
# print("Последовательность чисел кратных 5: ")
# print(z2_2(61))

# print("№2.3")
# print("Введите вещественное число:")
# a = float(input())
# print("Наименьшее натууральное n: ")
# print(z2_3(a))

# print("№2.4")
# print("Введите натуральное чилсло: ")
# x = int(input())
# print("Сумма и количесвто чисел: ",z2_4(x))

# print("№2.5")
# print(z2_5(4,2,6))

# print("№3.2")
# print("Введите числа a и b: ")
# a = int(input())
# b = int(input())
# print(z3_2(a,b))

# print("№3.3")
# print(z3_3(2,50))

# print("№3.4")
# print(z3_4(10))

# print("№5.1")
# a = int(input())
# b = int(input())
# print(z5_1(a,b,2))

# print("№5.2")
# print(z5_2(15))

print("№5.3")
sr_m, sr_f = z5_3()
print(f'Средний рост мальчиков {sr_m}, срединий рост девочек {sr_f}')