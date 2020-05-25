# What is a function in Python?
In Python, a function is a group of related statements that performs a specific task.

Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

####There are three types of functions in Python:

- Built-in functions, such as help() to ask for help, min() to get the minimum value, print() to print an object to the terminal,… You can find an overview with more of these functions here.
- User-Defined Functions (UDFs), which are functions that users create to help them out; And
- Anonymous functions, which are also called lambda functions because they are not declared with the standard def keyword.
Furthermore, it avoids repetition and makes the code reusable.

#### Syntax of Function
```bash
def function_name(parameters):
	"""docstring"""
	statement(s)
```
Here is an example to illustrate the scope of a variable inside a function.
```python
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)
```
Output:
```bash
Value inside function: 10
Value outside function: 20
```
#### Types of Functions
Basically, we can divide functions into the following two types:

- Built-in functions - Functions that are built into Python.
- User-defined functions - Functions defined by the users themselves
## Python Function Arguments
In Python, you can define a function that takes variable number of arguments. In this article, you will learn to define such functions using default, keyword and arbitrary arguments.
#### ArgumentsArguments
In the user-defined function topic, we learned about defining a function and calling it. Otherwise, the function call will result in an error. Here is an example.

```python
def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)

greet("Monica", "Good morning!")
```
Output:
```python
Hello Monica, Good morning!

```
## Variable Function Arguments
Up until now, functions had a fixed number of arguments. In Python, there are other ways to define a function that can take variable number of arguments.

Three different forms of this type are described below.

#### Python Default Arguments
Function arguments can have default values in Python.

We can provide a default value to an argument by using the assignment operator (=). Here is an example.
```python
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """


    print("Hello", name + ', ' + msg)
Variable Function Arguments
Up until now, functions had a fixed number of arguments. In Python, there are other ways to define a function that can take variable number of arguments.

Three different forms of this type are described below.

Python Default Arguments
Function arguments can have default values in Python.

We can provide a default value to an argument by using the assignment operator (=). Here is an example.

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")
```
**Output**

Hello Kate, Good morning!
Hello Bruce, How do you do?

## Python Keyword Arguments
When we call a function with some values, these values get assigned to the arguments according to their position.

For example, in the above function greet(), when we called it as greet("Bruce", "How do you do?"), the value "Bruce" gets assigned to the argument name and similarly "How do you do?" to msg.

Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed. Following calls to the above function are all valid and produce the same result.
```python
# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") 

1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")   
```
## Python Arbitrary Arguments
Sometimes, we do not know in advance the number of arguments that will be passed into a function. Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.

In the function definition, we use an asterisk (*) before the parameter name to denote this kind of argument. Here is an example.
```python
def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")
```
**Output**
```python
Hello Monica
Hello Luke
Hello Steve
Hello John

```


