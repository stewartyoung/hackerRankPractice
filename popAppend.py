myArray = [5,4,3,2,1]
numRotations = 4

def rotLeft(a, d):
    # we want to pop the first element, and append it to the end, d times
    for i in range(d):
        switchNumber = a.pop(0)
        a.append(switchNumber)
    return a

print(rotLeft(myArray, numRotations))