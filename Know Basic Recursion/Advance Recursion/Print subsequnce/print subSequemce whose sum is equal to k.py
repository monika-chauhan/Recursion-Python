def subSequence(ind, a, ds, k):
    res = []
    if ind == len(a):
        for i in ds:
            res.append(i)
        if sum(res) == k:
            print(res)
        return

    subSequence(ind + 1, a, ds, k)
    ds.append(a[ind])

    subSequence(ind + 1, a, ds, k)
    ds.remove(a[ind])


a = [1, 2, 1]
subSequence(0, a, [], 2)
