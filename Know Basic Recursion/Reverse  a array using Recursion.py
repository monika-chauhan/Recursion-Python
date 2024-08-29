# use of Two Pointer
def ReverseArr(a, l, r):
    if l >= r:
        return
    a[l], a[r] = a[r], a[l]
    ReverseArr(a, l + 1, r - 1)
    return a


a = [1, 2, 4, 3, 5]
print(ReverseArr(a, 0, len(a) - 1))


# Using pne pointer if we observed the l = 0 but r = (n-l-1) and once we reach half then return
def reverseArr(i, a, n):
    if i >= n // 2:
        return
    a[i], a[n - i - 1] = a[n - i - 1], a[i]
    reverseArr(i + 1, a, n)
    return a


a = [1, 2, 3, 4, 5]
print(reverseArr(0, a, len(a)))
