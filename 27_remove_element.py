from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        start_pointer, end_pointer = 0, len(nums) - 1
        counter = 0
        while start_pointer <= end_pointer:
            if nums[start_pointer] == val:
                nums[start_pointer], nums[end_pointer] = nums[end_pointer], nums[start_pointer]
                end_pointer -= 1
            else:
                counter += 1
                start_pointer += 1
        return counter
