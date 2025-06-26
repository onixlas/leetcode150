from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        result = []
        start = 0

        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1] + 1:
                if start == index - 1:
                    result.append(f'{nums[start]}')
                else:
                    result.append(f'{nums[start]}->{nums[index - 1]}')
                start = index

        if start == len(nums) - 1:
            result.append(f'{nums[start]}')
        else:
            result.append(f'{nums[start]}->{nums[-1]}')

        return result


assert Solution().summaryRanges([0,1,2,4,5,7]) == ["0->2","4->5","7"], 'Test 1 Failed'
assert Solution().summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"], 'Test 2 Failed'
