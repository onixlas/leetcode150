from typing import  List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        shots = 1
        current_point = points[0]

        for point in points:
            if point[0] > current_point[1]:
                shots += 1
                current_point = point
        return shots

assert Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]) == 2, 'Test 1 Failed'
assert Solution().findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]) == 4, 'Test 2 Failed'