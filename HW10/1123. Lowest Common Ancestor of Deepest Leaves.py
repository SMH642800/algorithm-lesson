"""
Given the root of a binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

  - The node of a binary tree is a leaf if and only if it has no children
  - The depth of the root of the tree is 0. if the depth of a node is d, the depth of each of its children is d + 1.
  - The lowest common ancestor of a set S of nodes, is the node A with the largest depth such that every node in S is in the subtree with root A.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def getDeepestLeave(root, leave):
            if not root: return None, leave

            left, left_leave = getDeepestLeave(root.left, leave+1)        
            right, right_leave = getDeepestLeave(root.right, leave+1)

            if left_leave == right_leave:
                return root, left_leave
            elif left_leave > right_leave:
                return left, left_leave
            else:
                return right, right_leave
            
        return getDeepestLeave(root, 0)[0]

