a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
if a%5==0 and b%5==0:
    print("both the no.s are divisible by 5")
elif a%5==0 or b%5 ==0:
    print("either one no is divisible by 5")
else:
    print("none the no.s are divisible by 5")