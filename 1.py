class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rui = [nums[0]]
        for i in range(1, len(nums)):
            rui.append(rui[i-1] + nums[i])
        return rui