# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def threeSumClosest(self, nums, target):		# O(N^2)
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0]+nums[1]+nums[2]
        for i in xrange(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == target:
                    return cur_sum
                
                if abs(cur_sum-target) < abs(res-target):
                    res = cur_sum
                
                if cur_sum < target:
                    j += 1
                elif cur_sum > target:
                    k -= 1
                    
        return res