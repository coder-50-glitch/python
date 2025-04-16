print("select u r ride")
print("1. bike")
print("2. car")
ch=int(input("enter u r choice"))
if(ch==1):
    print("what type of bike?")
    print("1. Scooty")
    print("2. Scooter")
    ch2=int(input("choose u r bike"))
    if(ch2==1):
        print("you hv selected scooty")
    else:
        print("you hv selected scooter")
elif(ch==2):
    print("enter type of car")
    print("1. sedan")
    print("2. XUV")
    ch3=int(input("enter u r choice"))
    if(ch3==1):
        print("u hv selected SEDAN")
    else:
        print("u hv selected XUV")
else:
    print("wrong choice")
