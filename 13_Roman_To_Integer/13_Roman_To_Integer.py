class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        ## Solution 1 (Efficient)
        ref = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        n = len(s)
        
        for i in range(n):
            if i < n - 1 and ref[s[i]] < ref[s[i + 1]]:
                sum -= ref[s[i]]
            else:
                sum += ref[s[i]]
        
        return sum
    
        # Solution 2 (Solved the problem but less efficient than the above)
        '''
        sum = 0
        ref = {"I":1,"V":5,"IV":4,"X":10,"L":50,"C":100,"D":500,"M":1000,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    
        while s != "":
            if len(s) != 1 and s[0] + s[1] in ref.keys():
                sum += ref[s[0] + s[1]]
                s = s[2:]
            else:
                sum += ref[s[0]]
                s = s[1:]
        return sum
        '''

solution = Solution()
# Example 3
print(solution.romanToInt("MCMXCIV"))