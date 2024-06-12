class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Solution 1 : 18 ms(Runtime) - 12 MB(Memory)
        if not strs:
            return ""
    
        prefix = strs[0]

        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix
    
        # Solution 2: 14 ms(Runtime) - 12 MB(Memory)
        '''
        if not strs:
            return ""
    
        min_length = min(len(s) for s in strs)
        
        low, high = 0, min_length
        
        while low <= high:
            mid = (low + high) // 2
            prefix = strs[0][:mid]
            if all(string.startswith(prefix) for string in strs):
                low = mid + 1
            else:
                high = mid - 1
        
        return strs[0][: (low + high) // 2]
        '''

        # Solution 3: 17 ms(Runtime) - 11.8 MB(Memory)
        '''
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for string in strs[1:]:
                if i == len(string) or string[i] != char:
                    return strs[0][:i]
        
        return strs[0]
        '''
        

solution = Solution()
# Example 1
print(solution.longestCommonPrefix(["flower","flow","flight"])) 

# Example 2
print(solution.longestCommonPrefix(["dog","racecar","car"]))