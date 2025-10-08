# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root,arr):
            if not root:
                return
            inorder(root.left,arr)
            arr.append(root.val)
            inorder(root.right,arr)
        def build_balanced_bst(nums):
            if not nums:
                return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = build_balanced_bst(nums[:mid])
            root.right = build_balanced_bst(nums[mid+1:])
            return root
        nums = []
        inorder(root,nums)
        return build_balanced_bst(nums)
