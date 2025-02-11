from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        total_profit = 0
        prev_price = prices[0]

        for price in prices[1:]:
            if price < prev_price:
                total_profit += prev_price - cur_min
                cur_min = price
            prev_price = price

        if prev_price > cur_min:
            total_profit += prev_price - cur_min

        return total_profit


assert Solution().maxProfit([1,2,3,4,5]) == 4
assert Solution().maxProfit([7,1,5,3,6,4]) == 7
assert Solution().maxProfit([7,6,4,3,1]) == 0
