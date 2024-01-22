class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        bit = 0
        m = 0
        for n in nums:
            if (bit >> n) & 1 == 1:
                m = n
            bit |= (1 << n)
        cnt = 1
        while bit > 0:
            if ((bit >> 1) & 1) == 0:
                mi = cnt
                break
            bit >>= 1
            cnt += 1
        return [m, mi]