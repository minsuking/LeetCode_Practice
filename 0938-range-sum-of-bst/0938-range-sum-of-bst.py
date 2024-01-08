# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        que = deque()
        que.append(root)
        res = 0
        while que:
            node = que.popleft()
            if low <= node.val <= high:
                res += node.val
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return res