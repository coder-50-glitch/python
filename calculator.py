def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def mul(p,q):
    return p*q
def div(p,q):
    p/q
print("enter u r choice")
print("a. add")
print("b. sub")
print("c. multiplication")
print("d. division")
ch= input("enter choice")
num1= int(input("enter 1st no"))
num2 = int(input("enter 2nd no"))
if ch== 'a':
    print(num1, "+", num2, "=", add(num1, num2))
elif ch=='b':
    print(num1, "-", num2, "=", sub(num1, num2))
elif ch == 'c':
    print(num1,"*", num2,"=", mul(num1, num2))
elif ch== 'd':
    print(num1,"/", num2, "=", div(num1, num2))
else:
    print("wrong choice")