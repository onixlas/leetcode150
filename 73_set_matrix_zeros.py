from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nlines = len(matrix)
        nrows = len(matrix[0])
        zero_lines = set()
        zero_rows = set()

        for line in range(nlines):
            for row in range(nrows):
                if matrix[line][row] == 0:
                    zero_lines.add(line)
                    zero_rows.add(row)

        for line in range(nlines):
            for row in range(nrows):
                if line in zero_lines or row in zero_rows:
                    matrix[line][row] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
assert matrix == [[1,0,1],[0,0,0],[1,0,1]], 'Test 1 Failed'
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]], 'Test 2 Failed'