# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]

# Output: 
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]

# Output: 
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.


class Solution(object):
    def findLongestWord(self, s, d):        # O(NXlogN + NX), O(logN) where n = # of words, x = average length
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x:(-len(x), x))
        for word in d:
            i, n = 0, len(word)
            for c in s:
                if i < n and word[i] == c:
                    i += 1
            
            if i == n:
                return word
        return ""
        


class Solution(object):
    def findLongestWord(self, s, d):    # O(NX), O(X)

        res = ''
        for word in d:
            i, n = 0, len(word)
            for c in s:
                if i < n and word[i] == c:
                    i += 1
            
            if i == n and (n > len(res) or (n == len(res) and word < res)):
                res = word
                
            
        return res
        