#Zad1
from typing import List


def kortsort(kortezh):
    check= True
    for i in kortezh:
        if (round(i) != i):
            check = False
            break
    if check:
        return sorted(kortezh)
    else:
        return kortezh

#Zad2
def kortrand(kortezh, searchNum):
    kortNew = ()
    check = False
    for i in kortezh:
        if (i == searchNum and check == False):
            check = True
            kortNew = kortNew+(i,)
            continue
        elif (i==searchNum and check == True):
            kortNew = kortNew+(i,)
            break

        if (check == True):
            kortNew = kortNew+(i,)
    return kortNew

#Zad3
def listadd(newlist):
    list = []
    for i in newlist:
        if i not in list:
            list.append(i)
    return sorted(tuple(list),reverse=True)

#Zad4
def kortEl(kortezh, element):
    temp = 0
    for i in kortezh:
        if i == element:
           return kortezh[0:temp]+kortezh[temp+1:kortezh.__sizeof__()]
        temp+=1
    return kortezh

#Zad5
def mnzhv(list):
    mnzh=set(list)
    power=len(mnzh)
    return mnzh,power

#Zad6
from collections.abc import Hashable
def Hasha(list):
    temp = 0
    mnzh=set()
    for i in list:
        if isinstance(i, Hashable):
            mnzh.add(i)
    return mnzh

#Zad7
def SimDif(l1,l2,l3):
    mn1=set(l1)
    mn2=set(l2)
    mn3=set(l3)
    mn12=mn1^mn2
    mn23=mn12^mn3
    return mn23

print(kortsort((1,4,2.2,3,5,6,1)))
print(kortrand((1,4,8,3,4,6,1),4))
print(listadd([2,3,3,2,5,7,4]))
print(kortEl((1,4,2,3,5,6,3),4))
print(mnzhv([1,5,4,3,5,3]))
print(Hasha([1,5,4,3,4,2]))
print(SimDif([1,9,5,2,4],[1,5,3,6,4],[1,7,2,0]))