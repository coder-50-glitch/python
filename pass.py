for x in range(10):
    if x%10 == 0:
        print("twist")
    elif x%15 == 0:
        print("pass")
    elif x%5 == 0:
        print("fizz")
    elif x%3 == 0:
        print("buzz")
    else:
        print(x)