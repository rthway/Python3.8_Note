# Run-Time Errors
Here are a few common run-time errors. Python is able to understand what the program says, but runs into problems when actually performing the instructions.

- using an undefined variable or function. This can also occur if you use capital letters inconsistently in a variable name:
```python
# An undefined variable
callMe = "Maybe"
print(callme)
```
- dividing by zero, which makes no sense in mathematics. (Why? Since 0 times any number is 0, there is no solution to 1 = X * 0, so 1/0 is undefined.)
```python
# Dividing by zero
print(1/0)
```
- using operators on the wrong type of data
```python
# Adding text and a number
print("you cannot add text and numbers" + 12)
```

