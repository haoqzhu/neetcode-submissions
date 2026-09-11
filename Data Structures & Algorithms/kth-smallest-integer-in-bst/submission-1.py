# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Create an array to keep track of all the values
        arr = []

        # Perform in-order traversal to add the values to the array from lowest to highest
        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        # Get the kth smallest (k - 1) and return
        return arr[k - 1]
