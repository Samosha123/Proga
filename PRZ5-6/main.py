#Zad1
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



print(kortsort((1,4,2.2,3,5,6,1)))
print(kortrand((1,4,8,3,4,6,1),4))
print(listadd([2,3,3,2,5,7,4]))
print(kortEl((1,4,2,3,5,6,3),4))
