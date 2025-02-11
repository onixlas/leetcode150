from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        cur_max = prices[0]
        profit = 0

        for price in prices[1:]:
            if price < cur_min:
                cur_min = price
                cur_max = cur_min
            if price > cur_max:
                cur_max = price
                profit = max(profit, cur_max - cur_min)

        return profit

print(Solution().maxProfit([3,2,6,5,0,3]))