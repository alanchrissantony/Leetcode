# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        dp=0
        def helper(current, mx):
            nonlocal dp
            if current:
                helper(current.left, mx+1)
                helper(current.right, mx+1)
                if mx>dp:
                    dp=mx
                
        helper(root, 1)
        return dp