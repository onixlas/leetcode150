from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        first_pointer = 0

        for second_pointer in range(1, len(nums)):
            if nums[second_pointer] == nums[first_pointer] and counter < 2:
                first_pointer += 1
                nums[first_pointer], nums[second_pointer] = nums[second_pointer], nums[first_pointer]
                counter += 1
            elif nums[second_pointer] != nums[first_pointer]:
                first_pointer += 1
                nums[first_pointer], nums[second_pointer] = nums[second_pointer], nums[first_pointer]
                counter = 1
        return first_pointer + 1