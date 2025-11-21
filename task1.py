#Task 1: Perform  basic mathematical operations
#Description:This program takes two inputs and performs basic mathematical operations on them

#Taking two input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Performing operation
addition = num1+num2
substraction = num1-num2
multiplication = num1*num2
if num2 != 0:
    division = num1/num2
else:
    division = "Undefined (cannot divide by zero)"

print("/n---Results---")
print(f"Addition: {addition}")
print(f"Substraction: {substraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
