# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        x = ord('a')
        a, b = [0]*26, [0]*26
        for i in xrange(n1):
            a[ord(s1[i])-x] += 1
            b[ord(s2[i])-x] += 1
            
        if a == b:
            return True
            
        for i in xrange(n1, n2):
            b[ord(s2[i-n1])-x] -= 1
            b[ord(s2[i])-x] += 1
            if a == b:
                return True
        return False
            