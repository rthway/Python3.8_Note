Python - Variable Types
Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.

Assigning Values to Variables
Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example −


	#!/usr/bin/python

	counter = 100          # An integer assignment
	miles   = 1000.0       # A floating point
	name    = "John"       # A string
	print counter
	print miles
	print name

Here, 100, 1000.0 and "John" are the values assigned to counter, miles, and name variables, respectively. This produces the following result −

100
1000.0
John


Multiple Assignment
Python allows you to assign a single value to several variables simultaneously. For example −

	a = b = c = 1
Here, an integer object is created with the value 1, and all three variables are assigned to the same memory location. You can also assign multiple objects to multiple variables. For example −

	a,b,c = 1,2,"john"
Here, two integer objects with values 1 and 2 are assigned to variables a and b respectively, and one string object with the value "john" is assigned to the variable c.

Standard Data Types
The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

Python has five standard data types −

	Numbers
	String
	List
	Tuple
	Dictionary
	Python Numbers
Number data types store numeric values. Number objects are created when you assign a value to them. For example −

	var1 = 1
	var2 = 10


Python Strings
Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator. For example −


	#!/usr/bin/python

	str = 'Hello World!'

	print str          # Prints complete string
	print str[0]       # Prints first character of the string
	print str[2:5]     # Prints characters starting from 3rd to 5th
	print str[2:]      # Prints string starting from 3rd character
	print str * 2      # Prints string two times
	print str + "TEST" # Prints concatenated string
	
	Output:
	Hello World!
	H
	llo
	llo World!
	Hello World!Hello World!
	Hello World!TEST

Python Lists
Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator. For example −

	#!/usr/bin/python

	list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
	tinylist = [123, 'john']

	print list          # Prints complete list
	print list[0]       # Prints first element of the list
	print list[1:3]     # Prints elements starting from 2nd till 3rd 
	print list[2:]      # Prints elements starting from 3rd element
	print tinylist * 2  # Prints list two times
	print list + tinylist # Prints concatenated lists

	Output:
	['abcd', 786, 2.23, 'john', 70.2]
	abcd
	[786, 2.23]
	[2.23, 'john', 70.2]
	[123, 'john', 123, 'john']
	['abcd', 786, 2.23, 'john', 70.2, 123, 'john']


Python Tuples
A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses.

The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists. For example −

	
	#!/usr/bin/python

	tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
	tinytuple = (123, 'john')

	print tuple           # Prints complete list
	print tuple[0]        # Prints first element of the list
	print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
	print tuple[2:]       # Prints elements starting from 3rd element
	print tinytuple * 2   # Prints list two times
	print tuple + tinytuple # Prints concatenated lists

	Output:
	('abcd', 786, 2.23, 'john', 70.2)
	abcd
	(786, 2.23)
	(2.23, 'john', 70.2)
	(123, 'john', 123, 'john')
	('abcd', 786, 2.23, 'john', 70.2, 123, 'john')



Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). For example −


	#!/usr/bin/python

	dict = {}
	dict['one'] = "This is one"
	dict[2]     = "This is two"

	tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


	print dict['one']       # Prints value for 'one' key
	print dict[2]           # Prints value for 2 key
	print tinydict          # Prints complete dictionary
	print tinydict.keys()   # Prints all the keys
	print tinydict.values() # Prints all the values

	Output:
	This is one
	This is two
	{'dept': 'sales', 'code': 6734, 'name': 'john'}
	['dept', 'code', 'name']
	['sales', 6734, 'john']
Dictionaries have no concept of order among elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.
