# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?


class Solution_simple(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a, b, c = 0, 0, 0
        for each in nums:
            if each == 0:
                a +=1
            elif each == 1:
                b +=1
            else:
                c+= 1
        
        nums[0:a]=[0]*a
        nums[a:a+b] = [1]*b
        nums[a+b:] = [2]*c
            


class Solution(object):
    def sortColors(self, nums):
        """
        Just like the Lomuto partition algorithm usually used in quick sort. 
        We keep a loop invariant that [0,i) [i, j) [j, ind) are 0s, 1s and 2s sorted in place for [0,ind). 
        Here ")" means exclusive. We don't need to swap because we know the values we want.
        """
        i = j = 0
        for ind in xrange(len(nums)):
            val = nums[ind]
            nums[ind] = 2
            if val < 2:
                nums[j] = 1
                j += 1
            if val < 1:
                nums[i] = 0
                i += 1
        