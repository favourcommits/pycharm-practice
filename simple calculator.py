num1 = int(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operator = input("Enter an operator (+,-,*,/)")

# perfom the calculation based on operator

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 !=0:
        result = num1/num2
    else:
        result = "Error!Division by zero!"
else:
    result= "invalid operator"
print(f"The result is : {result}")
