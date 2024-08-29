def PrintNto1(i, n):
    if i < 1:
        return
    print(i)
    PrintNto1(i - 1, n)


PrintNto1(5, 5)
