class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = {}
        for i in range(len(arr)):
            if arr[i] not in dic.keys():
                dic[arr[i]] = 0
            dic[arr[i]] += 1
        l = []
        for i in dic.keys():
            l.append([i, dic[i]])
        l = sorted(l, key=lambda x:(x[1]))
        cnt = 0
        while cnt < k:
            tmp = l.pop(0)[1]
            if cnt + tmp <= k:
                cnt += tmp
            elif cnt + tmp > k:
                l.append([0, 0])
                break
        return len(l)