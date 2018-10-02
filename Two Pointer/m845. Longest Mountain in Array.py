# Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

# B.length >= 3
# There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# (Note that B could be any subarray of A, including the entire array A.)

# Given an array A of integers, return the length of the longest mountain. 

# Return 0 if there is no mountain.

# Example 1:

# Input: [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: [2,2,2]
# Output: 0
# Explanation: There is no mountain.
# Note:

# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000
# Follow up:

# Can you solve it using only one pass?
# Can you solve it in O(1) space?


class Solution(object):
    def longestMountain(self, A):		# Two pass!
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        res = 0
        i= -1
        forward = {}
        for ind in xrange(n-1):
            if A[ind] < A[ind+1]:
                if i<0:
                    i = ind

            elif i> -1:
                forward[ind] = i
                i = -1

        i = n
        for ind in xrange(n-1, 0, -1):
            if A[ind] < A[ind-1]:
                if i == n:
                    i = ind
            elif i<n:
                if ind in forward:
                    res = max(res, i-forward[ind]+1)
                i = n
 
        return res


# Intuition:
# We have already many 2-pass or 3-pass problems, like 821. Shortest Distance to a Character.
# They have almost the same idea.
# One forward pass and one backward pass.
# Maybe another pass to get the final result, or you can merge it in one previous pass.

# Explanation:
# In this problem, we take one forward pass to count up hill length (to every point).
# We take another backward pass to count down hill length (from every point).
# Finally a pass to find max(up[i] + down[i] + 1) where up[i] and down[i] should be positives.

# Time Complexity:
# O(N)

    def longestMountain(self, A):
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])




# Follow up

# In this solution, I count up length and down length.
# Both up and down length are clear to 0 when A[i - 1] == A[i] or down > 0 && A[i - 1] < A[i].

    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res