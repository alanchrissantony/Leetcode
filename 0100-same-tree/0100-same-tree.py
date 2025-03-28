# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ap,aq=[],[]
        def helper_p(current):
            if current:
                ap.append(current.val)
                if current.left:
                    ap.append("left")
                if current.right:
                    ap.append("right")
                helper_p(current.left)
                helper_p(current.right)
        def helper_q(current):
            if current:
                aq.append(current.val)
                if current.left:
                    aq.append("left")
                if current.right:
                    aq.append("right")
                helper_q(current.left)
                helper_q(current.right)
            
        helper_p(p)
        helper_q(q)
        return ap==aq