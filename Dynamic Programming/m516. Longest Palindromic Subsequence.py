# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:

# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".


class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] +2
                    
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
        return dp[0][n-1]


class Solution(object):
    
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        self.memo = [[0 for _ in xrange(n)] for _ in xrange(n)]
        return self.helper(s, 0, n-1)
                    
    def helper(self, s, i, j):
        if self.memo[i][j]:
            return self.memo[i][j]
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            self.memo[i][j] = self.helper(s, i+1, j-1) +2
                    
        else:
            self.memo[i][j] = max(self.helper(s, i+1, j), self.helper(s, i, j-1))
        return self.memo[i][j]