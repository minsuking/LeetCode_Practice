class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        nums = set(nums)
        ans = 0
        for n in nums:
            if n-1 not in nums:
                cnt = 1
                while n+1 in nums:
                    cnt += 1
                    n += 1
                ans = max(ans,cnt)
        return ans