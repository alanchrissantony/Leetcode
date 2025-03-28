# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        dx_cnt = 0

        def helper(current):
            nonlocal dx_cnt
            if current:
                dx_cnt+=1
                helper(current.left)
                helper(current.right)
        helper(root)
        return dx_cnt