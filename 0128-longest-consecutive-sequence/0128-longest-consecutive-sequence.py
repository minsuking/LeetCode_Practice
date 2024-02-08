class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        check = set(nums)
        res = 0
        for n in nums:
            if n-1 not in check:
                cnt = 1
                while n+1 in check:
                    cnt += 1
                    n += 1
                res = max(res,cnt)
        return res