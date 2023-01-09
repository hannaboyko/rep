f = int(input("Enter first number: "))
s = int(input("Enter second number: "))

dev_by_two = []
dev_by_three = []
dev_by_four = []
dev_by_five = []
dev_by_six = []
for i in range(f, s):
    if i % 2 == 0:
        dev_by_two.append(i)
    if i % 3 == 0:
        dev_by_three.append(i)
    if i % 4 == 0:
        dev_by_four.append(i)
    if i % 5 == 0:
        dev_by_five.append(i)
    if i % 6 == 0:
        dev_by_six.append(i)
print("Dividible by 2: ", dev_by_two)
print("Dividible by 3: ", dev_by_three)
print("Dividible by 4: ", dev_by_four)
print("Dividible by 5: ", dev_by_five)
print("Dividible by 6: ", dev_by_six)
