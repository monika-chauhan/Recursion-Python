from collections import Counter


def backtrack(nums, counter, path, res):
    if len(path) == len(nums):
        res.append(path)
        return
    for key in counter:
        if counter[key]:
            counter[key] -= 1
            backtrack(nums, counter, path + [key], res)
            counter[key] += 1


def UniquePermutation(nums):
    res = []
    backtrack(nums, Counter(nums), [], res)
    return res


array = [1, 1, 2]
print(UniquePermutation(array))
