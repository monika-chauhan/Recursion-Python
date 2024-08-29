# Print the non - duplicates subset
# Brute Force Solution
def subset(ind, a, ds, ans):
    if ind == len(a):
        ans.add(tuple(ds))
        return
    ds.append(a[ind])
    subset(ind + 1, a, ds, ans)
    ds.pop()
    subset(ind + 1, a, ds, ans)
    return


def subsetII(a):
    ans = set()
    res = []
    a.sort()
    subset(0, a, [], ans)
    for i in ans:
        res.append(list(i))
    return res


a = [1, 2, 2]
print(subsetII(a))
