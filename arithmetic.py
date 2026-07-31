#input two numbers
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

#product of the two numbers
product = number1 * number2

#condition
if product <= 1000:
    print(f"Return {number1} and {number2}")
else:
    print(f"The sum is: {product}")    