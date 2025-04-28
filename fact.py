def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)
print("factorial of 0 ",fact(0))
print("factorial of 1 ",fact(1))
print("factorial of 2 ",fact(2))
print("factorial of 3 ",fact(3))