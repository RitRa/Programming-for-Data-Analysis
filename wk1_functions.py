# Rita Raher 21/09/18 week 1
# function for the Greatest Common Divisor
def gcd(a, b):
    while b > 0:
     a, b = b, a % b
    return(a)


print(gcd(50, 20))
print(gcd(22, 143))



