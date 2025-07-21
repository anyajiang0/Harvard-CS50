"""
Functions → verbs or actions that the computer can perform. 
For example, the print function takes the argument, "Hello, world," and prints it. 
"""

print("Hello, world")

"""
Input is anotehr function that takes a prompt as an argument. 
"""

name = input("What's your name?")
print(f"Hello, {name}")

"""
Variables are a container for values in the program.

In-line comments can be used as a to-do list to help the person accomplish the coding task.
This is called psuedocode. 
"""

# Ask the user for their name
name = input("What's your name?")

# print hello 
print(f"Hello, {name}")

"""
strings, known as 'str', are sequences of text. 

The print function automatically includes the argument end='\n'. The '\n'
indicaes that the print function will automatically create a line break when run. 

However, you can provide an argument for 'end' such that a new line is not created. 
"""

name = input("What's your name? ")
print("hello,", end="")
print(name)

"""
The most elegant way to use strings would be f strings. 

The f is a special indicator for python to treat the string a special way. F strings will be 
used quite frequently while taking cs50. 
"""
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")

"""
By using the strip method on a variable (for example, name = name.strip()),  any whitespace 
from the left and right of the user's input will be removed. 

By using the title method, the user's name will be title-cased. You can use multiple methods 
on a variable.
"""

"""
An integer is referred to as an int.
"""

x = input("Enter a number. ")
y = input("Enter another number. ")

z = x + y
print(z)

"""
However, the input is interpreted as a string. We will need to convert the sting into an integer. 
"""

x = input("Enter a number. ")
y = input("Enter another number. ")

# Convert the string into an integer 

z = int(x) + int(y)

print(z)

"""
A floating point value is a real number that has a decimal point. 
"""

# Change the code to support a float 
x = float(input("Enter a number. "))
y = float(input("Enter another number. "))

# Round the answer to the nearest integer 
z = round(x + y)

# Print the result 
print(f"{z:,}") # This creates a result where the outputted 'z' will include a comma. 

"""
Creating custom functions 


Functions can be created using the def keyword.
"""

# Starting code, ask the user for their name, remove the whitespace and add title capitalization 
name = input("What's your name? ").strip().title() 

# Print the output 
print(f"Hello, {name}!")

# Define a function that says hello.
def hello():
    print("hello")

name = input("What's your name? ").strip().title()
# Call the function 
hello()
print(name)

# now output using the function
hello(name) 