def divide_numbers(a, b):
    return a / b

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
while num2 == 0:
    num2 = int(input("Enter the second number again: "))
result = divide_numbers(num1, num2)
print(result)