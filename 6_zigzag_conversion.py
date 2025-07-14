class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        total_jump = 2 * (numRows - 1)
        result = []
        for row in range(numRows):
            if row in (0, numRows - 1):
                first_jump, second_jump = total_jump, total_jump
            else:
                first_jump = total_jump - 2 * row
                second_jump = total_jump - first_jump
            index = row
            jumps = 0
            while index <= len(s) - 1:
                result.append(s[index])
                index += (not jumps % 2) * first_jump + (jumps % 2) * second_jump
                jumps += 1
        return ''.join(result)

    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        current_row = 0
        direction = 1

        result = [[] for _ in range(numRows)]

        for character in s:
            result[current_row].append(character)
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction

        return ''.join([''.join(row) for row in result])


assert Solution().convert(s="PAYPALISHIRING", numRows=3) == "PAHNAPLSIIGYIR"
assert Solution().convert(s="PAYPALISHIRING", numRows=4) == "PINALSIGYAHRPI"
assert Solution().convert(s="A", numRows=1) == "A"
