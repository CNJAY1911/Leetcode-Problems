class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            num = x
            result = 0
            while num > 0:
                remainder = num % 10
                result = result * 10 + remainder
                num = num // 10
            return result == x

# Example usage and test cases
solution = Solution()

# Test case 1: Positive palindrome number
x1 = 121
print(f"Is {x1} a palindrome? {solution.isPalindrome(x1)}")  # Output: True

# Test case 2: Negative number
x2 = -121
print(f"Is {x2} a palindrome? {solution.isPalindrome(x2)}")  # Output: False

# Test case 3: Non-palindrome number ending with 0
x3 = 10
print(f"Is {x3} a palindrome? {solution.isPalindrome(x3)}")  # Output: False
