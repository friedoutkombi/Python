#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Character input
#Create a program that asks the user
#to enter their name
#and their age. Print out a message
#addressed to them that
#tells them the year that they will turn
#100 years old

#(str,num)->str,num
#MY SOLUTION
name=input("Enter your name ")
age=int(input("Enter your age "))
hundred=(100-age)+2017
print(name+" you will turn 100 in the year "+str(hundred))

#THEIR SOLUTION
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2017 - age)+100)
print(name + " will be 100 years old in the year " + year)
