def PrintNto1(i,n):
    if i > n:
        return
    PrintNto1(i+1,n)
    print(i)

PrintNto1(1,5)
