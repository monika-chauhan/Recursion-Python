# time complexity = O(2^n + 2^nlog2^n)
def subset(ind, a, ans, s=0):
    if ind == len(a):
        ans.append(s)
        return

    subset(ind + 1, a, ans, s + a[ind])
    subset(ind + 1, a, ans, s)


def subsetSumI(a):
    ans = []
    subset(0, a, ans)
    return sorted(ans)


a = [1, 2, 3]
print(subsetSumI(a))
