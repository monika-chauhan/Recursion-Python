# count the subsequence whose sum is equal to k
def subSeq(ind, a, s, k):
    if ind == len(a):
        if s == k:
            return 1
        else:
            return 0
    s += a[ind]
    l = subSeq(ind + 1, a, s, k)  # take

    s -= a[ind]
    r = subSeq(ind + 1, a, s, k)  # not take

    return l + r


a = [1, 2, 1]
k = 2
print(subSeq(0, a, 0, k))
