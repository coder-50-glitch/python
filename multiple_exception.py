num1, num2 = eval(input("enter 2 no separeted by comma  "))
res=num1/num2
print("result is ", res)

except SyntaxError:
    print("comma is missing. enter like this 12, 34 ")
except:
    print("wrong input ")
else:
    print("no exception")
finally:
    print("this will execute no matterv what ")