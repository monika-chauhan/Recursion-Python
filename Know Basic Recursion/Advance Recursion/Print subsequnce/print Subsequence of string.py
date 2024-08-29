# time = O(2^n)*n
def subsequence(ind, s, ansStr):
    res = ''
    ans = []
    if ind == len(s):
        for i in ansStr:
            res += i
        ans.append(res)
        print(ans)
        return

    subsequence(ind + 1, s, ansStr)  # take
    ansStr += s[ind]

    subsequence(ind + 1, s, ansStr)
    ansStr.replace(s[ind],'')


print(subsequence(0, 'abc', ''))
