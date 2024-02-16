class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        maps = {}
        l = 0
        for r in range(len(s)):
            if s[r] in maps:
                l = max(maps[s[r]], l)
            
            res = max(res, r - l + 1)
            maps[s[r]] = r + 1

        return res
            