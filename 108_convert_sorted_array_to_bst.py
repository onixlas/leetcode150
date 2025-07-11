from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def _build_tree(left_index, right_index):
            if left_index > right_index:
                return None
            middle = (left_index + right_index)// 2

            node = TreeNode(nums[middle])

            node.left = _build_tree(left_index=left_index, right_index=middle-1)
            node.right = _build_tree(left_index=middle+1, right_index=right_index)
            return node
        return _build_tree(0, len(nums) - 1)