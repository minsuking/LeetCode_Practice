from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sMap1 = defaultdict(int)
        sMap2 = defaultdict(int)
        c1, c2 = 0, 0
        for c in s1:
            sMap1[c] += 1
            c1 += 1
        l = 0
        for c in s2:
            sMap2[c] += 1
            c2 += 1
            if sMap1 == sMap2:
                return True
            if c1 == c2:
                sMap2[s2[l]] -=1
                c2 -= 1
                if sMap2[s2[l]] == 0:
                    del sMap2[s2[l]]
                l += 1
                
           
        return False