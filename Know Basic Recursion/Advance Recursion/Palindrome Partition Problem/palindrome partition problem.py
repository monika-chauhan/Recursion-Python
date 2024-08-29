def partition(s):
    res = []
    partitionHelper(0, s, [], res)
    return res


def partitionHelper(index, s, path, res):
    if index == len(s):
        res.append(path[:])
        return
    for i in range(index, len(s)):
        if isPalindrome(s, index, i):
            path.append(s[index:i + 1])
            partitionHelper(i + 1, s, path, res)
            path.pop()


def isPalindrome(s, start, end):
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True


s = 'aabb'
print(partition(s))
