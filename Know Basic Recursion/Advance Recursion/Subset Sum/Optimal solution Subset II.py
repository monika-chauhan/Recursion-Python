# time = O(2^n)*o(k)
def subset(ind, a, ds, ans):
    ans.append(ds[:])
    for i in range(ind, len(a)):
        if i != ind and a[i] != a[i - 1]:
            continue
        ds.append(a[i])
        subset(i + 1, a, ds, ans)
        ds.pop()


def subsetII(nums):
    ans = []
    nums.sort()
    subset(0, nums, [], ans)
    return ans


a = [1, 2, 2]
print(subsetII(a))
