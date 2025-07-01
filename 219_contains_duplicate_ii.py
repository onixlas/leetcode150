from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for index in range(len(nums)):
            if nums[index] not in hashmap:
                hashmap[nums[index]] = index
            else:
                if abs(hashmap[nums[index]] - index) <= k:
                    return True
                else:
                    hashmap[nums[index]] = index

        return False

assert Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3) == True, 'Test 1 Failed'
assert Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1) == True, 'Test 2 Failed'
assert Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2) == False, 'Test 3 Failed'
