# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.


class Solution(object):
    def countSubstrings(self, s):		# O(N^2)
        """
        :type s: str
        :rtype: int
        """
        
        res, n = 0, len(s)
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                dp[i][j] = s[i] == s[j] and (j-i<3 or dp[i+1][j-1])
                if dp[i][j]:
                    res += 1
        return res
            