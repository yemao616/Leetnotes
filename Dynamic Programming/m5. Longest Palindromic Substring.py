# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, n = '', len(s)
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            for j in xrange(i, n):
                dp[i][j] = s[i] == s[j] and (j-i<3 or dp[i+1][j-1])
                if dp[i][j] and j-i+1 > len(res):
                    res = s[i:j+1]
        return res
            

'''
Common mistake

Some people will be tempted to come up with a quick solution, which is unfortunately flawed (however can be corrected easily):

Reverse SS and become S&#x27;S 
′
 . Find the longest common substring between SS and S&#x27;S 
′
 , which must also be the longest palindromic substring.

This seemed to work, let’s see some examples below.

For example, SS = "caba", S&#x27;S 
′
  = "abac".

The longest common substring between SS and S&#x27;S 
′
  is "aba", which is the answer.

Let’s try another example: SS = "abacdfgdcaba", S&#x27;S 
′
  = "abacdgfdcaba".

The longest common substring between SS and S&#x27;S 
′
  is "abacd". Clearly, this is not a valid palindrome.
'''


    def longestPalindrome(self, s):

        if len(s)<2 or s==s[::-1]:
            return s
        n=len(s)
        start,maxlen=0,1
        for i in range(n):
            odd =s[i-maxlen-1:i+1] #len(odd)=maxlen+2
            even=s[i-maxlen:i+1]    #len(even)=maxlen+1
            if i-maxlen-1>=0 and odd==odd[::-1]:
                start=i-maxlen-1
                maxlen+=2
                continue
            if i-maxlen>=0 and even==even[::-1]:
                start=i-maxlen
                maxlen+=1
        return s[start:start+maxlen]