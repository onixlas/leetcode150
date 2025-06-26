from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        closest = 0
        furthest = 0
        while furthest < len(nums) - 1:
            next_furthest = 0
            for index in range(closest, furthest + 1):
                next_furthest = max(next_furthest, index + nums[index])
            steps += 1
            closest = furthest + 1
            furthest = next_furthest
        return steps


assert Solution().jump([2,3,1,1,4]) == 2, 'Test 1'
assert Solution().jump([2,3,0,1,4]) == 2, 'Test 2'
assert Solution().jump([0]) == 0, 'Test 3'
