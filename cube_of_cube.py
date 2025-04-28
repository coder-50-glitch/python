def cube(num):
    return num*num*num
def by_threeno(num):
    if num%3==0:
        return cube(num)
    else:
        return False
print (by_threeno(9))
print (by_threeno(4))