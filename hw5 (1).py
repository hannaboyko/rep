
n = int(input())  # строка
a = []
for i in range(n):
    a.append([0] * n)

for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 1
        elif i > j and i < j:
            a[i][j] = 0

for i in a:
    print(i)
