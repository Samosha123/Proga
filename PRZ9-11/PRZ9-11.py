#Zad1
#1.1
def z1_1(x):
    if x >=0:
        f= x**(1/2)+x**2
    else:
        f = 1/x
    return f
#1.2
def z1_2 (a,b):
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a
    return max,min
#1.3
def z1_3(m_birth,y_birth):
    m_today = 11
    y_today = 2021
    y_count = y_today - y_birth
    if m_today > m_birth:
        y_count-=1
    return y_count
#1.4
def z1_4 (x1_4,y1_4):
    if x1_4 < 0 and y1_4 <0:
        q_num = 3
    elif x1_4 < 0 and y1_4 >0: 
        q_num = 2
    elif x1_4 > 0 and y1_4 > 0:
        q_num = 1
    else:
        q_num = 43
    return q_num

#Zad2
#2.1
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
#2.2
def z2_2(x):
    x = 61
    a = 0
    while x >= a:
        print(a)
        a+=5
#2.3
def z2_3 (a):
    a = float(input())
    sum = 0.0
    n = 0
    while sum <= a:
        n += 1
        sum += 1/n
    return (n)
#2.4
def z2_4 (x):
    sum = 0
    while x % 10 != 0:
        sum = sum + x % 10
        x = int(x / 10)
    return sum
#2.5
def z2_5(k, s, start):
    res_num= []

    for i in range(start, 11):
        if int(str(i)[-1]) == k and i % s == 0:
            res_num.append(i)

    return res_num


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

# print("---------- Задание 2.1 ----------")

# numbers_2_1 = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

# result_2_1 = get_sum_and_col_in_list_numbers(numbers_2_1)

# print("Сумма чисел:", result_2_1[0], "| Количество введенных чисел:", result_2_1[1])

# print("---------- Задание 2.2 ----------")

# number_2_2 = int(input("Введите число: "))

# print("Последовательность x5 чисел меньше введенного числа:", get_x_5_numbers_at_n(number_2_2))

# print("---------- Задание 2.3 ----------")

# number_2_3 = float(input("Введите вещественное число: "))

# print("Наименьшее натуральное n:", get_min_in_sum_range(number_2_3))

# print("---------- Задание 2.4 ----------")

# number_2_4 = int(input("Введите натуральное число: "))
# result_2_4 = get_sum_and_length_of_number(number_2_4)

# print("Сумма цифр:", result_2_4[0], "| Количество цифр:", result_2_4[1])