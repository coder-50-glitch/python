prof_per=0.0
loss_per=0.02
cp=int(input("enter cost price"))
sp= int(input("enter selling price"))
if sp>cp:
    profit=sp=cp
    prof_per = profit*100/cp
    print("profit =",profit)
    print("profit percentage",prof_per)
else:
    loss=cp-sp
    loss_per=loss*100/cp
    print("loss= ", loss)
    print("loss percentage", loss_per)