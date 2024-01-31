class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps_ = dict()
        for i, v in enumerate(nums):
            if target-v in maps_:
                return [maps_[target-v],i]
            else:
                maps_[v] = i
                
                
            