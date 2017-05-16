##List information
>>> grades = [80, 90, 70]
>>> grades[0]
80
>>> grades[1]
90
>>> grades[2]
70
>>> grades[1:2]
[90]
>>> grades[0:2]
[80, 90]
>>> 90 in grades
True
>>> 60 in grades
False
>>> len(grades)
3
>>> min(grades)
70
>>> max(grades)
90
>>> sum(grades)
240
>>> subjects = ['bio', 'cs', 'math', 'history']
>>> len(subjects)
4
>>> min(subjects)
'bio'
>>> max(subjects)
'math'
>>> sum(subjects)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sum(subjects)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> street_address = [10, 'Main Street']
>>> for grade in grades:
	print(grade)

	
80
90
70
>>> for item in subjects:
	print(item)

	
bio
cs
math
history
>>> @
