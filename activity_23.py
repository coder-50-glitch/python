n=int(input("enter a no"))
t=n
l=0
print(n)
while(n>0):
    l=l+1
    n=int(n/10)
if(l>4):
    l=int(l/2)
    print(l)
    chk=0
    while(t>0):
        rem=t%10
        if(chk==l):
            mdl1=rem
        elif(chk==l-1):
            mdl2=rem
        t=int(t/10)
        chk=chk+1
prod=mdl1*mdl2
print("\nthe product of mid digits("+str(mdl1)+"*"+str(mdl2)+")=", prod)
