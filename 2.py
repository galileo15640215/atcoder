import statistics
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr)-1)//2]
        l = []
        while arr:
            if abs(arr[0] - m) < abs(arr[-1] - m):
                l.append(arr.pop(-1))
            elif abs(arr[0] - m) == abs(arr[-1] - m):
                l.append(arr.pop(-1))
            else:
                l.append(arr.pop(0))
        return l[:k]