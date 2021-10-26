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

print(kortsort((1,4,2.2,3,5,6,1)))