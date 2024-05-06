import math
def mySqrt(n):
    sRoot = math.sqrt(n)
    #sRoot = math.floor(sRoot)

    return sRoot

n = int(input("Enter any number : "))
print("The square root of ", n," is :", "{:.2f}".format(mySqrt(n)))