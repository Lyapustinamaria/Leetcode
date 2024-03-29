# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            # Check if the current nodes have the same value
            if p.val != q.val:
                return False
            # Recursively check left and right subtrees

            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
