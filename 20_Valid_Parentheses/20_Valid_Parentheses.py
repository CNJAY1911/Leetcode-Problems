class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Solution : 17 ms(Runtime) - 11.8 MB(Memory) - Using Stack
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack
    

solution = Solution()
# Example 1
print(solution.isValid("()"))

# Example 2
print(solution.isValid("()[]{}"))

# Example 3
print(solution.isValid("(]"))