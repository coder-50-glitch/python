st=input("enter the word")
ch=input("enter character")
i=0
c=0
while(i<len(st)):
    if(st[i]==ch):
        c=c+1
    i=i+1
print("no. of time", ch, "occured ", c)
