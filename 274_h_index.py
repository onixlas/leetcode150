from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        my_hash = {}

        for citation in citations:
            if citation:
                if citation not in my_hash:
                    my_hash[citation] = 1
                else:
                    my_hash[citation] += 1
        cum_sum = 0

        for key in sorted(my_hash.keys(), reverse=True):
            cum_sum += my_hash[key]
            my_hash[key] = cum_sum
        max_cite = 0
        for key in sorted(my_hash.keys()):
            max_cite = max(max_cite, min(key, my_hash[key]))
        return max_cite


assert Solution().hIndex([3,0,6,1,5]) == 3, 'Test 1 Failed'
assert Solution().hIndex([1,3,1]) == 1, 'Test 2 Failed'
assert Solution().hIndex([100]) == 1, 'Test 3 Failed'
