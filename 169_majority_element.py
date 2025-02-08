from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        current_majority = nums[0]

        for num in nums[1:]:
            if num != current_majority:
                if counter == 0:
                    current_majority = num
                    counter = 1
                else:
                    counter -= 1
            else:
                counter += 1
        return current_majority
