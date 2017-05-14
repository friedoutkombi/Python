#List Less Than Ten
#http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

#Take a list and write a program that prints out
#all the elements of the list that are
#less than 5

#EXTRAS
#1.Make a new list that has all the elements
#less than 5 and print it out
#2. Do it in one line of Python
#3. Ask user for a number and return a list
#that contains only elements smaller than
#that given number.

###MY SOLUTION
inputlist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in inputlist:
    if element<5:
        print(element)

###MY SOLUTION + EXTRA 1
inputlist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
outputlist=[]

for element in inputlist:
    if element<5:
        outputlist.append(element)

print (outputlist)


##MY SOLUTION + EXTRA 1/3
inputlist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
outputlist=[]
inputnumber=int(input("Pick a number for elements to be less than "))

for element in inputlist:
    if element<inputnumber:
        outputlist.append(element)

print (outputlist)


##THEIR SOLUTION
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(raw_input("Choose a number: "))

new_list = []

for i in a:
	if i < num:
		new_list.append(i)

print new_list
