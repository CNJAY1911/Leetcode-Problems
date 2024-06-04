class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # Solution 1 : 41 ms(Runtime) - 12.5 MB(Memory) - Using HashMap
        indices = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                return [indices[complement], i]
            indices[num] = i
        return []
    
        # Solution 2 : 787 ms(Runtime) - 12.4 MB(Memory) - Using List Comprehension
        """
        result = [i for i in range(len(nums)) if target - nums[i] in nums[:i] + nums[i+1:]]
        return result
        """


solution = Solution()

# Taking input from Example 1
nums = [2, 7, 11, 15]                       
target = 9

print(solution.twoSum(nums, target))