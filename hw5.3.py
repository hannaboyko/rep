def fullWordFromList(x):
    full = ''.join(x)
    return full

leters = ["L", "i", "s", "t","i","k"]
result=fullWordFromList(leters)
print(result)


def fullWordInt(x):
    fullWord = ''.join([str(int) for int in x])
    return fullWord

newList= ["L", "i", "s", "t","i","k",2,1,2,3]
result=fullWordInt(newList)
print(result)