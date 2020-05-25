
# read fruits.txt file using python
file =open("fruits.txt", "r")
content =file.read()
file.close()
print(content)

# Read file and count lines
file = open("fruits.txt", "r")
con = file.readlines()
file.close()
for i in con:
    print(len(i.strip()))

#eg. 2 even better, you could treat both the temperature input and the file path as function arguments:
temperatures = [10, -20, -289, 100]


def writer(temperatures, filepath):
    with open(filepath, 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n")


writer(temperatures, "temps.txt")  # Here we're calling the function, otherwise no output will be generated
