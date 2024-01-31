from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_ = defaultdict(int)
        for i, n in enumerate(nums):
            if n in map_ and n * 2 == target:
                return [map_[n], i]
            map_[n] = i

        
        for i, n in enumerate(nums):
            if target - n in map_ and map_[target - n] != i:
                return [map_[target - n], i]
                
                
            