number = int(input("enter a number for multiply: \n"))
if number <= 100:
    print("Number is correct")
    print(f"Multiplication table for number:{number}")
else:
    "Try again"

for a in range(1, 10, 1):
    result = number * a
    print(number, "*", a, "=", result)
