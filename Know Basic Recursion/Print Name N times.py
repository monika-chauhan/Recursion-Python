def printName(i,n):
    if i > n:
        return
    print('Monika')
    printName(i+1,n)

printName(1,5)