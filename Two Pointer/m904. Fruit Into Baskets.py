# In a row of trees, the i-th tree produces fruit with type tree[i].

# You start at any tree of your choice, then repeatedly perform the following steps:

# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

# What is the total amount of fruit you can collect with this procedure?

 

# Example 1:

# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# Example 2:

# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# Example 3:

# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# Example 4:

# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

# Note:

# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length






# Problem
# "Start from any index, we can collect at most two types of fruits. What is the maximum amount"

# Translation
# Find out the longest length of subarrays with at most 2 different numbers?

# Solution of sliding window will be easier to understand.
# Here I share another solution wihtout hash map.
# Hope it's not damn hard to understand.

# Explanation:
# Loop all fruit c in tree,
# Note that a and b are the last two different types of fruit that we met,
# c is the current fruit type,
# so it's something like "....aaabbbc..."

# Case 1 c == b:
# fruit c already in the basket,
# and it's same as the last type of fruit
# cur += 1
# count_b += 1

# Case 2 c == a:
# fruit c already in the basket,
# but it's not same as the last type of fruit
# cur += 1
# count_b = 1
# a = b, b = c

# Case 3 c != b && c!= a:
# fruit c not in the basket,
# cur = count_b + 1
# count_b = 1
# a = b, b = c

# Of course, in each turn we need to update res = max(res, cur)

# Complexity:
# O(N) time, O(1) space


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        
        res = cur_b = cur = 0   # note: cur_b is the number of items between a and c!
        a = b = -1
        for c in tree:
            if c == b:
                cur += 1
                cur_b += 1
            else:
                if c == a:
                    cur += 1
                else:
                    cur = cur_b + 1
                cur_b = 1
                a, b = b, c
            res = max(res, cur)
        return res
