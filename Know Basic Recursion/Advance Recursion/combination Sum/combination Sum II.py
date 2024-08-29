# Not duplicates in combination whose sum equal to target
# time = O(2^n)*k
# space =O(n)*k
def combination(ind, candidates, target, ds, ans):
    if target == 0:
        ans.append(ds[:])
        return

    for i in range(ind, len(candidates)):
        # For not pick the duplicate element
        if i > ind and candidates[i] == candidates[i - 1]:
            continue
        if candidates[i] > target:
            break
        ds.append(candidates[i])
        combination(i + 1, candidates, target - candidates[i], ds, ans)
        ds.pop()


def combinationSumII(candidates, target):
    candidates = sorted(candidates)
    ans = []
    combination(0, candidates, target, [], ans)
    return ans


candidates = [2, 5, 2, 1, 2]
target = 5
print(combinationSumII(candidates, target))
