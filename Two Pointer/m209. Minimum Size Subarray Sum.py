# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.



class Solution(object):
    def minSubArrayLen(self, s, nums):		# O(N)
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res, j, cur_sum = n+1, 0, 0
        for i in xrange(n):
            cur_sum += nums[i]
            while cur_sum >= s:
                res = min(res, i-j+1)
                cur_sum -= nums[j]
                j += 1
        if res > n:
            return 0
        return res


# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
# O(NLogN) - search if a window of size k exists that satisfy the condition

class Solution(object):					# Binary Search O(NlogN)
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i, j, res = 1, n, n+1
        while i <= j:
            mid = (i+j)/2
            if self.window_exists(mid, s, nums):
                res = mid
                j = mid-1
            else:
                i = mid+1
        if res > n:
            return 0
        return res
    
    def window_exists(self, size, s, nums):
        cur_sum = 0
        for i in xrange(len(nums)):
            if i >= size:
                cur_sum -= nums[i-size]
            cur_sum += nums[i]
            if cur_sum >= s:
                return True
        return False
        

    
        