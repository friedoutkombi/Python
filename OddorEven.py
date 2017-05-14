#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#ODD OR EVEN

#Ask the user for a number.
#Depending on whether the number
#is even or odd, print out an
#appropriate message to the user.
#Hint: how does an even / odd number
#react differently when divided by 2?

#Extras:

#1. If the number is a multiple of 4,
#print out a different message.
#2. Ask the user for two numbers: one number
#to check (call it num) and one number to
#divide by (check). If check divides evenly
#into num, tell that to the user.
#If not, print a different appropriate message.

#MY SOLUTION (WITHOUT EXTRAS)
number=int(input("Please enter a number "))
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")

#MY SOLUTION (WITH EXTRA 1)
number=int(input("Please enter a number "))
if number%4==0:
    print("Number is even and divisble by 4")
else:
    if number%2==0:
        print("Number is even")
    else:
        print("Number is odd")

#MY SOLUTION (WITH EXTRA 2)
num=int(input("Please enter a number "))
check=int(input("Please enter a number to divide by "))

if num%check==0:
    print(str(check)+" divides evenly into "+str(num))
else:
    print(str(check)+" does not divide evenly into "+str(num))
