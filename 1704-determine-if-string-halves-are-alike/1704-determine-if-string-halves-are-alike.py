class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowers = set(['a','e','i','o','u','A','E','I','O','U'])
        a = 0
        b = 0
        l, r = 0, len(s) // 2
        while r < len(s):
            if s[l] in vowers:
                a += 1
            if s[r] in vowers:
                b += 1
            l += 1
            r += 1
        return a == b