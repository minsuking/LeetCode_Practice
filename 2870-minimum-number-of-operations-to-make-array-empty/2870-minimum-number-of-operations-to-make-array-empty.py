class Solution:
    def minOperations(self, nums: List[int]) -> int:
        map_ = defaultdict(int)
        for n in nums:
            map_[n] += 1
        res = 0
        cnt = 0
        for value in map_.values():
            if value == 1:
                return -1
            else:
                if value%3 == 0:
                    res += value//3 
                else:
                    res += value//3 + 1
        return res