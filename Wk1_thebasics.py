# Rita Raher 20/09/18 week 1
# if else statement revision
import datetime as d

today = d.datetime.today()
dayofweek = today.weekday()

print("Let's check if it's Tuesday?")

if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday tomorrow!")

else:
    print("Unfortunately, It's not Tuesday")

print("Thanks for checking if it's Tuesday!")



# While loops
# greatest common divisor

a = 50 
b = 20 
# runs over and over while the condition is true
while b > 0:
    a, b = b, a % b
print(a)
    