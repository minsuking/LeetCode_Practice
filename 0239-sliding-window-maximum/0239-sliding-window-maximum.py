class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        dpLeft = [0] * length
        dpRight = [0] * length
        
        left, right = nums[0], nums[-1]
        for i, num in enumerate(nums):
            if i % k == 0 :
                left = num
            if left <num:
                left = num
            dpLeft[i] = left
        
        for i in range(length-1,-1,-1):
            if i % k == k - 1:
                right = nums[i]
            if right < nums[i] : 
                right = nums[i]
            dpRight[i] = right
        
        res = []
        for i in range(length-k + 1):
            ii = i + k - 1
            res.append(max(dpRight[i], dpLeft[ii]))
        
        return res