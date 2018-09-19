

# Write a function that takes a string as input and returns the string reversed.

# Example 1:

# Input: "hello"
# Output: "olleh"
# Example 2:

# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"






class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, j = 0, len(s)-1
        res = [' ']*(j+1)
        
        while i <= j:
            res[i], res[j] = s[j], s[i]
            i += 1
            j -=1
        return ''.join(res)
            




class Solution(object):
    def reverseString(self, s):
        revstr = []
        for index in range(len(s)-1, -1, -1):
            revstr.append(s[index])
        return ''.join(revstr)



class Solution(object):
    def reverseString(self, s):
 
        return s[::-1]