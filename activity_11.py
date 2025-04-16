ch=str(input("did you have medical cause y/n"))
att= int(input("attendance"))
if(ch=="y"):
    print("you are allowed")
else:
    if(att>=75):
        print("allowed")
    else:
        print("not allowed")
    