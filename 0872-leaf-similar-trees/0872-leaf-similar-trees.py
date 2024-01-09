# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            res = []
            if root.left == None and root.right == None:
                return [root.val]
            if root.left:
                res.extend(dfs(root.left))
            if root.right:
                res.extend(dfs(root.right))
            return res
        
        return dfs(root1) == dfs(root2)
        