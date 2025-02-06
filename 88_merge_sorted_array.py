from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first_index, second_index = m - 1, n - 1
        runner = m + n - 1

        while second_index >= 0:
            if first_index >= 0 and nums1[first_index] > nums2[second_index]:
                nums1[runner] = nums1[first_index]
                runner -= 1
                first_index -= 1
            else:
                nums1[runner] = nums2[second_index]
                runner -= 1
                second_index -= 1
