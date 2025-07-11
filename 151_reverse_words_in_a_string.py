class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ' '.join(s)


assert Solution().reverseWords("the sky is blue") == "blue is sky the", 'Test 1 Failed'
assert Solution().reverseWords("  hello world  ") == "world hello", 'Test 2 Failed'
assert Solution().reverseWords("a good   example") == "example good a", 'Test 3 Failed'
