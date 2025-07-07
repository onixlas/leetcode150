from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        length = len(gas)
        current_tank = 0
        start = -1
        for index in range(length):
            current_tank += gas[index] - cost[index]
            if current_tank < 0:
                start = -1
                current_tank = 0
            elif start == -1:
                start = index
        return start

assert Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3, 'Test 1 Failed'
assert Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]) == -1, 'Test 2 Failed'
assert Solution().canCompleteCircuit(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]) == 4, 'Test 3 Failed'
assert Solution().canCompleteCircuit(gas=[3, 1, 1], cost=[1, 2, 2]) == 0, 'Test 4 Failed'
assert Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5, 5, 70], cost=[2, 3, 4, 3, 9, 6, 2]) == 6, 'Test 5 Failed'