# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        self.res = 0
        def helper(root, cMax, cMin):
            if root == None:
                return
            
            self.res = max(self.res, abs(cMax - root.val), abs(cMin - root.val))
            cMax = max(cMax, root.val)
            cMin = min(cMin, root.val)
            helper(root.left, cMax, cMin)
            helper(root.right, cMax, cMin)
        helper(root, root.val, root.val) 
        return self.res