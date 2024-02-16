class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        check = set()
        res = 0
        while r < len(s):
            if s[r] in check:
                check.remove(s[l])
                l += 1
            else:
                check.add(s[r])
                r += 1
            res = max(res,r - l)
        return res
            