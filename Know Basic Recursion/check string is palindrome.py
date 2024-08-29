# Using Two Pointer
def palinStr(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palinStr(s, l + 1, r - 1)


string = 'MADAM'
print(palinStr(string, 0, len(string) - 1))


# using one pointer
def PalinString(s, i, n):
    if i >= n // 2: return True
    if s[i] != s[n - i - 1]:
        return False
    return PalinString(s, i + 1, n)


s = 'MACDAM'
print(PalinString(s, 0, len(s)))
