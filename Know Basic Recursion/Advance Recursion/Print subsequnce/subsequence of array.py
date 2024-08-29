# using recursion Take and not take
def subsequence(ind, arr, ds):
    res = []
    if ind == len(arr):
        for i in ds:
            res.append(i)
        print(res)
        return

    subsequence(ind + 1, arr, ds)  # take
    ds.append(arr[ind])

    subsequence(ind + 1, arr, ds)  # not take
    ds.remove(arr[ind])



a = [3, 2, 1]
subsequence(0, a, [])
