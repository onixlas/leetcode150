class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        s_length = len(s)
        if not s_length:
            return True

        for t_pointer in range(len(t)):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            if s_pointer == s_length:
                return True

        return False

assert Solution().isSubsequence(s='abc', t='ahbgdc') == True, 'Test 1 Failed'
assert Solution().isSubsequence(s='axc', t='ahbgdc') == False, 'Test 2 Failed'
assert Solution().isSubsequence(s='', t='ahbgdc') == True, 'Test 3 Failed'