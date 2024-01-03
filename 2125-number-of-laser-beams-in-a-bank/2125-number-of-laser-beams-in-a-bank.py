class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        pre = 0
        for b in bank:
            curr = b.count('1')
            if curr > 0:
                res +=  curr * pre
                pre = curr
        return res