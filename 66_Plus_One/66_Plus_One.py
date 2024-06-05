class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in digits:
            num = num * 10 + i
        result = [int(i) for i in str(num+1)]
        return result

    def test(self):
        # Example 1
        digits1 = [1, 2, 3]
        print(self.plusOne(digits1))  # Output: [1, 2, 4]

        # Example 2
        digits2 = [4, 3, 2, 1]
        print(self.plusOne(digits2))  # Output: [4, 3, 2, 2]

        # Example 3
        digits3 = [9]
        print(self.plusOne(digits3))  # Output: [1, 0]


# Run test
solution = Solution()
solution.test()
