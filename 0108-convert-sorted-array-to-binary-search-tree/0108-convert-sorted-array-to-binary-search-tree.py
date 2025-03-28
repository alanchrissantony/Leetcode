# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
            self.root=None


    def append(self, data):
            node=TreeNode(data)
            if self.root is None:
                self.root=node
                return
            current=self.root
            while True:
                if data<current.val:
                    if current.left:
                        current=current.left
                    else:
                        current.left=node
                        break
                else:
                    if current.right:
                        current=current.right
                    else:
                        current.right=node
                        break

    def split(self, nums):
        if len(nums)>=1:
            mid=len(nums)//2
            self.append(nums[mid])
            del nums[mid]
            left=nums[:mid]
            right=nums[mid:]
        
            self.split(left)
            self.split(right)
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        self.split(nums)    

        return self.root
        