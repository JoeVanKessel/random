def ksmallest(k, datastream):
    if k > len(datastream):
        k = len(datastream)
    ans = [None]*k
    i = 0
    j = 0
    for x in ans:
        if x == None:
            ans.insert(j, datastream[j])
            del ans[-1]
            j += 1

    while i < len(datastream):
        j = 0
        if i+1 < len(datastream):
            i += 1
        else:
            return ans
        while j < len(ans):
            if datastream[i] < ans[j]:
                ans.insert(j, datastream[i])
                del ans[-1]
                break
            else:
                j += 1
