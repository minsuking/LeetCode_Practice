from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map_ = defaultdict(int)
        for n in arr:
            map_[n] += 1
        set_ = set()
        for k, v in map_.items():
            if v in set_:
                return False
            set_.add(v)
        return True