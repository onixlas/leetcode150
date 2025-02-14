from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_goal = len(nums) - 1

        for index in range(len(nums) - 2, -1, -1):
            if index + nums[index] >= current_goal:
                current_goal = index

        return current_goal == 0

assert Solution().canJump([2,3,1,1,4]) == True
assert Solution().canJump([3,2,1,0,4]) == False