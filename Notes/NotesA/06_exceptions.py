# Exceptions (use me sparingly please)

# Exception - condition that results in abnormal program flow
# Exception handling - what we actively do for an exception
# Throw/Raise - abnormal conditions throw or raise an exception
# Catch - Code that handles the abnormal condition
# Unhandled exceptions - program killers.  Thrown... but not caught.

"""
# Divide by zero error (ZeroDivisionError)
x = 0
y = 2

try:
    print(y / x)
except:
    print("Invalid operation, divide by zero.")

# Conversion error (ValueError)
done = False

while not done:
    try:
        user_input = int(input("Enter a valid integer: "))
        done = True
    except:
        print("Number not valid, enter an integer")


# File opening (IOError, FileNotFoundError)

try:
    file = open("AliceInWonderland.txt")
except:
    print("File not found.")


# Use the built in error types for Python

try:
    #my_file = open("myfile.txt")
    #print(1 / 0)
    int("Hello")
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Fool! You can't divide by zero")
except ValueError:
    print("Invalid int conversion")
except:
    print("Unknown Error")



# Make an MPG calculator

try:
    miles = float(input("Miles traveled: "))
    gallons = float(input("Gallons used: "))
except ValueError:
    print("You entered an invalid number.")


try:
    print("MPG is", miles / gallons)
except:
    print("Your MPG is infinite!!!")
finally:
    print("Finally will always run regardless of exception or no exception")


# FORMATTING

# round

print(round(323.1234341,2))

# format method (a string method)
a = 234.53465
b = 12.34
print("My number is {}".format(a))
print("My number is {1} and = {0}".format(a, b)) # able to specify the order
"""
import random
# justification and spacing
for i in range(20):
    c = random.randrange(2000)
    print("{:6}".format(c)) # six spaces are reserved for the number
    print("**{:^30}**".format(c))  # 30 spaces and centered
# commas
for i in range(20):
    c = random.randrange(10000000)
    print("${:8,}".format(c))

# precision and datatype (d dec/int, f float, b binary)
for c in range(20):
    c = random.random() * 1000
    print("{:.3f}".format(c))

