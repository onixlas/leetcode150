class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False

        hashmap = {}

        for char, word in zip(pattern, s):
            if char not in hashmap:
                hashmap[char] = word
            else:
                if hashmap[char] != word:
                    return False

        hashmap2 = {}
        for char, word in zip(pattern, s):
            if word not in hashmap2:
                hashmap2[word] = char
            else:
                if hashmap2[word] != char:
                    return False

        return True


assert Solution().wordPattern(pattern="abba", s="dog cat cat dog") == True, 'Test 1 Failed'
assert Solution().wordPattern(pattern="abba", s="dog cat cat fish") == False, 'Test 2 Failed'
assert Solution().wordPattern(pattern="aaaa", s="dog cat cat dog") == False, 'Test 3 Failed'
assert Solution().wordPattern(pattern="abba", s="dog dog dog dog") == False, 'Test 4 Failed'