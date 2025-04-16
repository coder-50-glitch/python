no=int(input("enter no"))
temp=no
s=0
while(no>0):
    d=no%10
    s=s+d**3
    no=no//10
if(temp==s):
    print("amstrong no")
else:
    print("not amstrong no")  
    