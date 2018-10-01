# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = list(s)
        i, j = 0, len(l)-1
        while i < j:
            a, b = l[i].lower(), l[j].lower()
            if a in vowels:
                if b in vowels:
                    l[i], l[j] = l[j], l[i]
                    i += 1
                j -= 1
            elif b in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(l)
              


class Solution(object):
    def reverseVowels(self, s):
        slist = list(s)
        vowel_set = set(list("aeiouAEIOU"))
        left = 0
        right = len(s) - 1 
        while left < right:
            while slist[left] not in vowel_set and left != right:
                left += 1 
            while slist[right] not in vowel_set and left != right:
                right -= 1 
            if left != right:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1 
                right -= 1 
        return "".join(slist)