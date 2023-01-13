def sameElement(a,b,c):
    for i in a:

        for j in b:
            if i == j:
                c.append(i)

    if len(c) == 0:
        c.append("None")

    return c


firstList=[1,2,3,"foo"]
secondList=[2,"foo",6,7]
c=[]
result = sameElement(firstList,secondList,c)
print(c)