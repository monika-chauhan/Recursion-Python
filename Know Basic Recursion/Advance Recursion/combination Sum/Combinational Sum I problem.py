# Using Recursion :-> make the combination using

def combination(ind, arr, target, ds, ans):
    if ind == len(arr):
        if target == 0:
            ans.append(list(ds))
        return

    if arr[ind] <= target: # Pick the element
        ds.append(arr[ind])
        combination(ind, arr, target - arr[ind], ds, ans)
        ds.pop()     # Come back and pop the element 
    combination(ind + 1, arr, target, ds, ans)


def combinationSumI(candidates, target):
    ans = []
    combination(0, candidates, target, [], ans)
    return ans


a = [2, 3, 6, 7]
target = 7
print(combinationSumI(a, target))
