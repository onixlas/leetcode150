from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def _is_mirror(node_left: Optional[TreeNode],
                       node_right: Optional[TreeNode]) -> bool:
            if not node_left and not node_right:
                return True

            if not node_left or not node_right:
                return False

            return ((node_left.val == node_right.val) and
                    _is_mirror(node_left.left, node_right.right) and
                    _is_mirror(node_left.right, node_right.left))

        return _is_mirror(root.left, root.right)
