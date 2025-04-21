low = int(input("enter lower range"))
high = int(input("enter upper range"))
for i in range (low, high+1):
    c=0
    for j in range(1,i+1):
        if(i%j==0):
            c=c+1
    if(c==2):
        print(i, end=' ')