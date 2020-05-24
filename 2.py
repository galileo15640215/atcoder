class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sl = len(s)
        cnt = 0
        st = ['a', 'e', 'i', 'o', 'u']
        ma = 0
        for i in range(k):
            if s[i] in st:
                cnt += 1
        if ma < cnt:
            ma = cnt
        for i in range(k, sl):
            if s[i] in st:
                cnt += 1
            if s[i-k] in st:
                cnt -= 1
            if ma < cnt:
                ma = cnt
        return ma