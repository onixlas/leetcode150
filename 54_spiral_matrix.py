from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for index in range(left, right + 1):
                result.append(matrix[top][index])

            top += 1

            for index in range(top, bottom + 1):
                result.append(matrix[index][right])

            right -= 1

            if top <= bottom:
                for index in range(right, left  - 1, -1):
                    result.append(matrix[bottom][index])

                bottom -= 1

            if left <= right:
                for index in range(bottom, top - 1, -1):
                    result.append(matrix[index][left])
                left += 1

        return result


assert Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5], 'Test 1 Failed'
assert Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7], 'Test 2 Failed'