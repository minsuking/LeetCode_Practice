class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = 10**4 + 1
        res = 0
        for price in prices:
            if pre < price:
                res = max(res,price-pre)
            pre = min(pre, price)
        return res