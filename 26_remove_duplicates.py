from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        first_pointer, second_pointer = 0, 0
        counter = 1

        while second_pointer < len(nums):
            if nums[second_pointer] == nums[first_pointer]:
                second_pointer += 1
            else:
                first_pointer += 1
                nums[first_pointer], nums[second_pointer] = nums[second_pointer], nums[first_pointer]
                second_pointer += 1
                counter += 1
        return counter
