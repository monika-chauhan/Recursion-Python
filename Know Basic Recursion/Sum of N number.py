# Parametersied Recursion
def SumN(n,sum):
    if n == 0:
        print(sum)
        return
    SumN(n-1,sum+n)
SumN(3,0)

def SumNnumber(n):
    if n == 0:
        return 0
    return n + SumNnumber(n-1)
print(SumNnumber(3))
