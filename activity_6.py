a=float(input("enter height"))
b=float(input("enter weight"))      
bmi=b/(1/100)**2
print ("your bmi is: ",bmi)
if bmi<=18.4:
    print("u r under weight")
elif bmi <=24.9:
    print("u r healthy")
elif bmi<=29.9:
    print("u r overweight")
elif bmi<=34.9:
    print("u r severly over weight")
elif bmi<=39.9:
    print("u r obese")
else:
    print("u r severly obese")