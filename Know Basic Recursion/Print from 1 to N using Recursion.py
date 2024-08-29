def Print1ToN(i, n):
    if i > n:
        return
    print(i)
    Print1ToN(i + 1, n)


Print1ToN(1, 5)
