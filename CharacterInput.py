#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

#Character input
#Create a program that asks the user
#to enter their name
#and their age. Print out a message
#addressed to them that
#tells them the year that they will turn
#100 years old

#(str,num)->str,num

name=input("Enter your name ")
age=int(input("Enter your age "))
hundred=(100-age)+2017
print(name+" you will turn 100 in the year "+str(hundred))

