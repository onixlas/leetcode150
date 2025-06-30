class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s = {}
        hash_t = {}

        for index in range(len(s)):
            if s[index] not in hash_s:
                hash_s[s[index]] = index
            if t[index] not in hash_t:
                hash_t[t[index]] = index
            if hash_t[t[index]] != hash_s[s[index]]:
                return False

        return True


assert Solution().isIsomorphic('egg', 'add') == True, 'Test 1 Failed'
assert Solution().isIsomorphic('foo', 'bar') == False, 'Test 2 Failed'


