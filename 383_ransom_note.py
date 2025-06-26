class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for character in magazine:
            if character not in hashmap:
                hashmap[character] = 1
            else:
                hashmap[character] += 1
        for character in ransomNote:
            if character not in hashmap or hashmap[character] == 0:
                return False
            else:
                hashmap[character] -= 1
        return True



assert Solution().canConstruct(ransomNote='a', magazine='b') == False, 'Test 1 Failed'
assert Solution().canConstruct(ransomNote='aa', magazine='ab') == False, 'Test 2 Failed'
assert Solution().canConstruct(ransomNote='aa', magazine='aab') == True, 'Test 3 Failed'