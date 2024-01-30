class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pCheck = 0
        nCheck = 0
        mask = 0
        for n in nums:
            mask = (1 << abs(n))
            
            if n >= 0: 
                if pCheck & mask:
                    return True
                else:
                    pCheck |= mask
            else:
                if nCheck & mask:
                    return True
                else:
                    nCheck |= mask
                
        return False