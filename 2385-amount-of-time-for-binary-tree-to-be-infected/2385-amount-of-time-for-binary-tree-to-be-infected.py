# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)
        def helper(root):
            if root == None:
                return 
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
            
            helper(root.left)
            helper(root.right)
        helper(root)
        que = deque()
        que.append((0,start))
        visited = set()
        visited.add(start)
        res = -1
        while que:
            depth, node = que.popleft()
            res = max(res, depth)
            for nei in graph[node]:
                if nei not in visited:
                    que.append((depth+1,nei))
                    visited.add(nei)
                    
        return res