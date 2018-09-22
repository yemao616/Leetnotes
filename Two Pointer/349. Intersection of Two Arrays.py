# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.



class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = list(set(nums1) & set(nums2))
        return res
            

class Solution(object):
    def intersection(self, nums1, nums2):

        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i<len(nums1) and j<len(nums2):
            a, b = nums1[i], nums2[j]
            if a < b:
                i += 1
            elif b < a:
                j += 1
            else: 
                if not len(res) or a != res[-1]:
                    res.append(a)
                i += 1
                j += 1
        
        return res
            