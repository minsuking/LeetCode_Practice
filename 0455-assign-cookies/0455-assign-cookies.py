class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        t = 0
        for i in range(len(g)):
            for j in range(t, len(s)):
                if g[i] <= s[j]:
                    res += 1
                    t = j + 1
                    break
        return res