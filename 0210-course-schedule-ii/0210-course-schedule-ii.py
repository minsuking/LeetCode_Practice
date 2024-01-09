from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for v1, v2 in prerequisites:
            graph[v2].append(v1)
            indegree[v1] += 1
        
        que = deque()
        visited = set()
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
                visited.add(i)
        
        res = []
        while que:
            node = que.popleft()
            res.append(node)
            for nei in graph[node]:
                if nei not in visited:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        que.append(nei)
                        visited.add(nei)
        return res if len(res) == numCourses else []
                    
                    