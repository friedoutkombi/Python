#Ex 4: Divisors
#http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

#Create a program that asks the user for a number and then prints out
#a list of all the divisors of that number. (If you don’t know
#what a divisor is, it is a number that divides evenly into
#another number. For example, 13 is a divisor of 26 because 26 / 13
#has no remainder.)

#>>>Please enter a number: 20
#1
#2
#4
#5
#10
#20

###MY SOLUTION
number=int(input("Please enter a number: "))
x=[]
for i in range(1,number+1):
    if number%i==0:
        x.append(i)

for elem in x:
    print(elem)

###THEIR SOLUTION
num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
