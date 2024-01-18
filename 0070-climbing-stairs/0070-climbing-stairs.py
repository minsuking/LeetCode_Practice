class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 2
        if n==1:
            return p1
        if n==2:
            return p2
        for i in range(3,n+1):
            res = p1 + p2
            p1, p2 = p2, res
        return res