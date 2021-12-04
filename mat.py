ar=[]

with open('mat.txt', 'r', encoding='utf-8') as r:
    for i in r:
        ar.append(i[:-1])
