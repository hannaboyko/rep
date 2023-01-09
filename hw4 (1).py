condition = True
sum_val = 0
while condition:
    a = input("Enter a numbers  \n")
    if a == "end":
        condition = False
        break
    sum_val += int(a)

    print(sum_val)