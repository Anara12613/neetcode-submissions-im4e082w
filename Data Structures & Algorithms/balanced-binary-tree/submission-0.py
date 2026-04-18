# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def hight(root):
            if not root:
                return 0
            return 1 + max(hight(root.left),hight(root.right))
        if not root:
            return True
        
        left_h = hight(root.left)
        right_h = hight(root.right)
        if abs(left_h-right_h) >1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        