# Invalid Syntax in Python
When you run your Python code, the interpreter will first parse it to convert it into Python byte code, which it will then execute. The interpreter will find any invalid syntax in Python during this first stage of program execution, also known as the parsing stage. If the interpreter can’t parse your Python code successfully, then this means that you used invalid syntax somewhere in your code. The interpreter will attempt to show you where that error occurred.

When you’re learning Python for the first time, it can be frustrating to get a SyntaxError. Python will attempt to help you determine where the invalid syntax is in your code, but the traceback it provides can be a little confusing. Sometimes, the code it points to is perfectly fine.
You can’t handle invalid syntax in Python like other exceptions. Even if you tried to wrap a try and except block around code with invalid syntax, you’d still see the interpreter raise a SyntaxError.

## SyntaxError Exception and Traceback
When the interpreter encounters invalid syntax in Python code, it will raise a SyntaxError exception and provide a traceback with some helpful information to help you debug the error. Here’s some code that contains invalid syntax in Python:
```python
# theofficefacts.py
ages = {
    'pam': 24,
    'jim': 24
    'michael': 43
}
print(f'Michael is {ages["michael"]} years old.')
```
You can see the invalid syntax in the dictionary literal on line 4. The second entry, 'jim', is missing a comma. If you tried to run this code as-is, then you’d get the following traceback:
```shell
$ python theofficefacts.py
File "theofficefacts.py", line 5
    'michael': 43
            ^
SyntaxError: invalid syntax
```
Note that the traceback message locates the error in line 5, not line 4. The Python interpreter is attempting to point out where the invalid syntax is. However, it can only really point to where it first noticed a problem. When you get a SyntaxError traceback and the code that the traceback is pointing to looks fine, then you’ll want to start moving backward through the code until you can determine what’s wrong.

In the example above, there isn’t a problem with leaving out a comma, depending on what comes after it. For example, there’s no problem with a missing comma after 'michael' in line 5. But once the interpreter encounters something that doesn’t make sense, it can only point you to the first thing it found that it couldn’t understand.

## Common Syntax Problems
- Misusing the Assignment Operator (=)
- Misspelling, Missing, or Misusing Python Keywords
- Missing Parentheses, Brackets, and Quotes
- Defining and Calling Functions
- Changing Python Versions

- Mistaking Dictionary Syntax like: 
```python
ages = dict(pam=24)
 ages
{'pam': 24}
```
- Using the Wrong Indentation

```python
# indentation.py
def foo():
    for i in range(10):
        print(i)
  print('done')

foo()
```





