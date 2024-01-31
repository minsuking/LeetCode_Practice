class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps_ = dict()
        for i, n in enumerate(nums):
            if target-n in maps_:
                return [maps_[target-n], i]
            else:
                maps_[n] = i
                
                
            