def minimum(x):
    secondMin = x[0]
    minVal = x[0]
    for i in range(len(x)):
        if x[i] < minVal:
            minVal = x[i]

    #print(minVal)  # для проверки

    for i in range(len(x)):
        if x[i] < secondMin and x[i] != minVal:
            secondMin = x[i]

    return secondMin




y = [555,24,65,633,12,10]
l= minimum(y)
print(l)