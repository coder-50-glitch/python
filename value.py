try:
    no=int(input("enter a no"))
    print("the no is ", no)
except ValueError as ex:
    print("exception ", ex)