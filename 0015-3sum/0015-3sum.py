from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pos, neg = [], []
        map_ = defaultdict(int)
        res = set()
        for n in nums:
            map_[n] += 1
        
        if 0 in map_ and map_[0] >= 3:
            res.add((0,0,0))
        
        for k, v in map_.items():
            if k > 0 :
                pos.append(k)
            if k < 0:
                neg.append(k)
        
        for p in pos:
            for n in neg:
                t = -(p + n)
                if t in map_:
                    if (t != p and t != n) or map_[t] > 1:
                        res.add(tuple(sorted([t,n,p])))
        return list(res)