def Print1ToN(i, n):
    if i < 1:
        return
    Print1ToN(i - 1, n)
    print(i)


Print1ToN(5, 5)
