from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        for s in strs:
            graph[tuple(sorted(s))].append(s)
        return graph.values()