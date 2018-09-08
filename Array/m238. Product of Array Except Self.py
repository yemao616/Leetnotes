# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)



class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre, post, n = 1, 1, len(nums)      # pre and post save the product before/after current num
        output = []
        
        for i in xrange(n):
            output.append(pre)
            pre *= nums[i]
            
        for i in xrange(n-1, -1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output