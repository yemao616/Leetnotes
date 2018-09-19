# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:

# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.




class Solution(object):
    def partitionLabels(self, S):   # O(N)+O(1)
        """
        :type S: str
        :rtype: List[int]
        """
        
        last = {c:i for i, c in enumerate(S)}
        a = b = 0
        res = []
        
        for i, c in enumerate(S):
            b = max(b, last[c])
            if i == b:
                res.append(b-a+1)
                a = i+1
                
        return res



# Algorithm:
# first pass to record the last occurence of each char
# second pass to find the partition, using a and b to record the current start and end index.