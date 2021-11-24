#Функция, запомянающая в массив элементы введенного числа number
import math
def func (number):
    mass = []
    countNum = len(str(number)) - 1
    divider = 10**countNum
    for i in range(0,countNum + 1):
        temp = math.floor(number / divider)
        mass.append(temp % 10)
        divider /= 10
    return mass
print(func(864456374332)) 