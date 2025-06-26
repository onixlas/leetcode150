from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length

        def _rotate(ns: List[int], start: int, end: int) -> None:
            while start < end:
                ns[start], ns[end] = ns[end], ns[start]
                start += 1
                end -= 1

        _rotate(nums, start=0, end=length - 1)
        _rotate(nums, start=0, end=k - 1)
        _rotate(nums, start=k, end=length - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(nums, 3)
assert nums == [5, 6, 7, 1, 2, 3, 4], 'Test 1 Failed'
nums = [-1, -100, 3, 99]
Solution().rotate(nums, 2)
assert nums == [3, 99, -1, -100], 'Test 2 Failed'
nums = [-1]
Solution().rotate(nums, 2)
assert nums == [-1], 'Test 3 Failed'