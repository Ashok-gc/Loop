num = int(input("Enter the number for factorial: "))
product=1
for i in range(num, 0, -1):
    product = product * i
print(f"The factorial of {num} is {product}")
