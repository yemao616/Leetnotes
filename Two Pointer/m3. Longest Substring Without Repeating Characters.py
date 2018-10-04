# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):		# O(N)
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        j, res = 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                j = max(j, dic[ch]+1)  # j records the current start_index
                
            dic[ch] = i
            res = max(res, i-j+1)
        return res


 '''
 keep a hashmap which stores the characters in string as keys and their indices as values, and keep two pointers which define the max substring. 
 move the right pointer to scan through the string , and meanwhile update the hashmap. 
 If the character is already in the hashmap, then move the left pointer to the right of the same character last found
 '''