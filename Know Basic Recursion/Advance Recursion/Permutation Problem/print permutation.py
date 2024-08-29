# time = O(fact(n))*n
# Space = O(1)
def permutation(ind, nums, ans):
    if ind == len(nums) - 1:
        ans.append(list(nums))
        return

    for i in range(ind, len(nums)):
        nums[ind], nums[i] = nums[i], nums[ind]
        permutation(ind + 1, nums, ans)
        nums[i], nums[ind] = nums[i], nums[ind]


def printPermutaton(nums):
    ans = []
    permutation(0, nums, ans)
    return ans


a = [1, 2, 3]
print(printPermutaton(a))
