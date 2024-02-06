class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        res[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i+1] * nums[i+1]
        pre = 1
        for i in range(len(nums)):
            res[i] = res[i] * pre
            pre = pre*nums[i]
        
        return res