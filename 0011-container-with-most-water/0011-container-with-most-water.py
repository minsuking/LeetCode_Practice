class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = -1
        while l < r:
            dis = r - l
            if height[l] < height[r]:
                m = l
                l += 1
            else:
                m = r
                r -= 1
            res = max(res, height[m] * dis)
        return res