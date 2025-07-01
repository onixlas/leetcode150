class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        my_stack = []
        #print(path)
        for part in path:
            if part == '..':
                if my_stack:
                    my_stack.pop()
            elif part == '.' or not part:
                pass
            else:
                my_stack.append(part)

        return '/' + '/'.join(my_stack)

assert Solution().simplifyPath("/home/") == "/home", 'Test 1 Failed'
assert Solution().simplifyPath("/home//foo/") == "/home/foo", 'Test 2 Failed'
assert Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures", 'Test 3 Failed'
assert Solution().simplifyPath("/../") == '/', 'Test 4 Failed'
assert Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d", 'Test 5 Failed'