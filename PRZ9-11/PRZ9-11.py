import math

pbda = []
pab = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
pb = [0, 0, 0, 0]
padb = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
ha = 0 
hb = 0
hadb = 0 
hbda = 0

print("\nВведите матрицу P(b/a):")
for i in range(0, 4): 
    pbda.append(list(map(float, input(str(i + 1) + " линия: ").split()))) 

pa = list(map(float, input("Введите все P(a) через пробел: ").split()))

print("\nМатрица P(a,b):") 
for i in range(0, 4):
    for j in range(0, 4): 
        pab[i][j] = pbda[i][j] * pa[j] 
        print(round(pab[i][j], 4), end=",\t") 
    print("")

print("\nP(b):") 
for i in range(0, 4): 
    for j in range(0, 4): 
        pb[i] += pab[j][i] 
    print(round(pb[i], 4), end=",\t")
print("\n")

print("Матрица P(a/b):") 
for i in range(0, 4): 
    for j in range(0, 4): 
        padb[i][j] = pab[i][j] / pb[j] 
        print(round(padb[i][j], 4), end=",\t") 
    print("") 
print("")

for i in range(0, 4): 
    if pa[i] != 0: 
        ha += pa[i] * math.log2(pa[i]) 
ha *= -1 
print("H(A):", round(ha, 5))

for i in range(0, 4): 
    if pb[i] != 0: 
        hb += pb[i] * math.log2(pb[i]) 
hb *= -1 
print("H(B):", round(hb, 5))

for i in range(0, 4): 
    for j in range(0, 4): 
        if padb[i][j] != 0: 
            hadb += pb[i] * padb[i][j] * math.log2(padb[i][j]) 
hadb *= -1 
print("H(A/B):", round(hadb, 5))

for i in range(0, 4): 
    for j in range(0, 4): 
        if pbda[i][j] != 0: 
            hbda += pa[i] * pbda[i][j] * math.log2(pbda[i][j]) 
hbda *= -1

print("H(B/A):", round(hbda, 5)) 

CA = 100 * (ha - hadb) 
CB = 100 * (hb - hbda) 
print("C = n[H(A) - H(A/B)]:", round(CA, 5)) 
print("C = n[H(B) - H(B/A)]:", round(CB, 5))