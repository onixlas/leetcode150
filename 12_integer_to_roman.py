class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        result = []

        for value, symbol in value_symbols:
            if num == 0:
                break

            count = num // value
            result.append(symbol * count)

            num -= value * count

        return ''.join(result)


assert Solution().intToRoman(58) == 'LVIII', 'Test 1 Failed'
assert Solution().intToRoman(1994) == 'MCMXCIV', 'Test 2 Failed'

