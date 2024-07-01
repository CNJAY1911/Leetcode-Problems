from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Binary Search Algorithm to find the correct position for the target in the sorted list. 
        # Runtime - 40 ms, Memory - 17.05 MB
        min, max = 0, len(nums) - 1

        while min <= max:
            mid = (min + max) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                min = mid + 1
            else:
                max = mid - 1
        
        return min
    
    
solution = Solution()

# Example 1

nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))   # Output: 2

# Example 2

nums = [1, 3, 5, 6]
target = 2
print(solution.searchInsert(nums, target))   # Output: 1

# Example 3

nums = [1, 3, 5, 6]
target = 7
print(solution.searchInsert(nums, target))   # Output: 4
