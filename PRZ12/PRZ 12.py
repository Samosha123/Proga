#Zad1
def ceasar(text, shift):   
    ans = ' '
    for letter in text:
        if(letter != ' '):
            ans += " ".join(chr(ord(letter)+shift))
        else:
            ans += " ".join(' ')
    return ans
try:
    text = input("Введите предложение: ")
    shift = int(input("Введите сдвиг: "))
    
    encoded = ceasar(text, shift)
    decoded = text
    print("Зашифрованная строка:", encoded)
    print("Расшифрованная строка:", decoded)
except ValueError as err:
    print("Ошибка:", err, ". Проверьте введённые данные")
except Exception as err:
        print("Ошибка:", err)
#Zad2      
def power(x, y=2):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except ValueError as err:
    print("Ошибка:", err, "Проверьте введённые данные")
except Exception as err:
    print("Ошибка:", err)
            
def zad_3(): 
    try:
        n = int(input("Введите кол-во человек: "))
        
        middle_names = {}
        for i in range(n):
            fio = input("Введите ФИО через пробел: ").split()
            if i in range(n):
                middle_name = fio[2]
                middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        print("Самое популярное отчество:", sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
        print("В расчете участвовало человек:", n)
    except ValueError as err:
        print("Ошибка:", err, "Проверьте введённые данные.")
    except Exception as err:
        print("Ошибка:", err)

def zad_4():
    необходимые_экзамены = {
        "Информатика": 80,
        "Математика": 85,
        "Русский язык": 75
    }

    print("""Для определения возможности поступления, необходима информация о Вас.

    Для ввода экзамена и баллов введите их через |: Химия | 40.
    Для завершения ввода нажмите Enter.
    """)
    try:
        сданные_экзамены = {}
        while True:
            ввод = input("").strip()
            if ввод == "":
                break
    
            экзамен, балл = [x.strip() for x in ввод.split("|")]
            сданные_экзамены[экзамен] = int(балл)
    
        print("Ваши экзамены:")
        for i, (экзамен, балл) in enumerate(сданные_экзамены.items(), start=1):
            print("{}) {} {}".format(i, экзамен, балл))
    
        ok = False
        
        for необходимый_экзамен, баллы in необходимые_экзамены.items():
            if сданные_экзамены[необходимый_экзамен] < баллы:
                break
            else:
                ok = True
        print("Вы можете к нам поступить!" if ok else "Увы...")
    except ValueError as err:
        print("Ошибка:", err, "Проверьте введённые данные.")
    except Exception as err:
        print("Ошибка:", err)


print("\nЗадание 3")
zad_3()

print("\nЗадание 4")
zad_4()