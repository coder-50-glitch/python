l=[12,4,3,6,10,7]
print("original list ", l)
cont = 0
for i in l:
    cont+=i
print("sum of list element ", cont)
avg = cont/len(l)
print("average ", avg)
l.sort()
print(l[0])
print("\n", l[-1])