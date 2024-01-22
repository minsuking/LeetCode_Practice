# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        que = deque()
        que.append((root, 2**31, -2**31-1))
        while que:
            node, mx, mn = que.popleft()
            if node.val >= mx or node.val <= mn:
                return False
            if node.left:
                que.append((node.left, node.val, mn))
            if node.right:
                que.append((node.right, mx, node.val))
        return True