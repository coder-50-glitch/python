u=int(input("enter unit consumed"))
if(u<50):
    amt=u*2.6
elif(u<=100):
    amt=130+(u-50)*3.25
elif(u<=200):
    amt=130+50*3.25*(u-100)*5.26
else:
    amt=130+50*3.25+100*5.26+(u-200)*8.45
amt=amt+35
print("bill = ", amt)