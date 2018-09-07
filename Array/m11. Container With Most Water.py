# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.


# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

 

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

# Idea / Proof:

# The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
# All other containers are less wide and thus would need a higher water level in order to hold more water.
# The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.

class Solution_origin:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water



class Solution(object): # updated versiton by reducing the number of comparisons
    def maxArea(self, height):
    
        water = 0
        i, j = 0, len(height)-1
        
        while i < j:
            left, right = height[i], height[j]
            
            if left < right:
                cur_water = (j-i)*left
                i += 1
            else:
                cur_water = (j-i)*right
                j -=1
            water = max(water, cur_water)
        
        return water