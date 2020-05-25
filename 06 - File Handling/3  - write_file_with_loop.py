# Q.convert temperature c to f and write to temp.txt files
# f=c*9/5+32
temperatures = [10,-20,-289,100]

def c_to_f(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c>-273.8:
                f=c*9/5+32
                file.write(str(f) + "\n")
c_to_f(temperatures)