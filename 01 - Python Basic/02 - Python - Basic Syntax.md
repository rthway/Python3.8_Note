# Python - Basic Syntax

The Python language has many similarities to Perl, C, and Java. However, there are some definite differences between the languages.
Let us execute programs in different modes of programming to print Hello, Python!.

#### Interactive Mode Programming :

	>>> print "Hello, Python!"
	
	Output:
	Hello, Python!

Script Mode Programming
Invoking the interpreter with a script parameter begins execution of the script and continues until the script is finished. When the script is finished, the interpreter is no longer active.

Let us write a simple Python program in a script. Python files have extension .py. Type the following source code in a test.py file 

	print "Hello, Python!"
	Save as a test.py
	gotu terminal
	$ python test.py

	Output:
	Hello, Python!


#### Comments in Python:
A hash sign (#) that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.

	# First comment
	print "Hello, Python!" # second comment

Following triple-quoted string is also ignored by Python interpreter and can be used as a multiline comments:

	'''
	This is a multiline
	comment.
	'''


#### Multi-Line Statements
Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character (\) to denote that the line should continue. For example −

	total = item_one + \
	        item_two + \
	        item_three
Statements contained within the [], {}, or () brackets do not need to use the line continuation character. For example −

	days = ['Monday', 'Tuesday', 'Wednesday',
	        'Thursday', 'Friday']


#### Quotation in Python
Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all the following are legal −

	word = 'word'
	sentence = "This is a sentence."
	paragraph = """This is a paragraph. It is
	made up of multiple lines and sentences."""

#### Waiting for the User
The following line of the program displays the prompt, the statement saying “Press the enter key to exit”, and waits for the user to take action −

	input("\n\nPress the enter key to exit.")
Here, "\n\n" is used to create two new lines before displaying the actual line. Once the user presses the key, the program ends. This is a nice trick to keep a console window open until the user is done with an application.

