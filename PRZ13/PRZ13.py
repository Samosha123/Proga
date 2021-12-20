import math
def z1_1():
    n = int(input("Введите числа: "))
    mass = []
    countNum = len(str(n)) - 1
    divider = 10**countNum
    for i in range(0,countNum + 1):
        temp = math.floor(n / divider)
        mass.append(temp % 10)
        divider /= 10
    with open('text.txt', 'w') as f:
        for i in mass:
            f.write(str(i) + '\n')
        f.close()
    with open('text.txt', 'r') as f:
        print(f.read())
        f.close()
      
     
def z1_2():
    try:
        with open('text.txt', 'r') as f:
            max1 = max(map(float, f))
            f.close()
        with open('text.txt', 'r') as f:  
            result = sum(map(float, f))
            f.close()
        with open('text.txt', 'a') as f:
            f.write(str(result) + '\n')
            f.write(str(max1)+ '\n')
            f.close()
        with open('text.txt', 'r') as f:
             print(f.read())
             f.close()
    except Exception:
        print("Ошибка при работе с файлом")
    except FileNotFoundError:
        print("Файл не найден")        
        
def z1_3():
    try:
        sum1 = 0
        max1 = 0
        with open('text.txt', 'r') as f:
              for i in f:
                  for j in i.split():
                      try:
                          if j.isnumeric() or j.replace('.', '',1).isdigit():
                              sum1 += float(j)
                              if float(j) > max1:
                                  max1 = float(j)
                      except Exception:
                          pass
        f.close()
        with open('text.txt', 'a') as f:
            f.write(str(sum1) + '\n')
            f.write(str(max1)+ '\n')
            f.close()
        with open('text.txt', 'r') as f:
             print(f.read())
             f.close()
    except Exception:
        print("Ошибка при работе с файлом")
    except FileNotFoundError:
        print("Файл не найден")     
  
def z1_4():
    try:
        gl = "уеыаоэяию"
        sg = "йцкнгшщзхъфвпрлджчсмтьб"
        glk = sgk = 0
        with open('stih.txt', 'r', encoding='utf-8') as f:
           a = f.read()
           print(a)
           a = a.split()
           for i in a:
               if i[0] in gl:
                   glk +=1
               if i[0] in sg:
                   sgk +=1
           f.close()
        if glk > sgk:
            print("Слов начинающихся на гласную больше:", glk)
        elif sgk > glk:
            print("Слов начинающихся на согласную больше:", sgk)
        else:
            print("Слов на гласную и согласную одинаково")
    except Exception:
        print("Ошибка при работе с файлом")
    except FileNotFoundError:
        print("Файл не найден")
        
print("Задание 1: ")
z1_1() 

print("Задание 2: \n") 
z1_2()

print("Задание 3: \n")
z1_3()

print("Задание 4: \n")
z1_4()