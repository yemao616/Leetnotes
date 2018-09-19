
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.


# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

# Note:

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000


class Solution(object):
    def sortArrayByParity(self, A): O(N)+O(N)
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for each in A:
            if each%2 == 0:
                even.append(each)
            else:
                odd.append(each)
        even.extend(odd)
        return even


# In-place Algorithm

# We'll maintain two pointers i and j. The loop invariant is everything below i has parity 0 (ie. A[k] % 2 == 0 when k < i), and everything above j has parity 1.

# Then, there are 4 cases for (A[i] % 2, A[j] % 2):

# If it is (0, 1), then everything is correct: i++ and j--.

# If it is (1, 0), we swap them so they are correct, then continue.

# If it is (0, 0), only the i place is correct, so we i++ and continue.

# If it is (1, 1), only the j place is correct, so we j-- and continue.

class Solution(object):  # O(N)+O(1)
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A)-1
        while i < j:
            if A[i]%2 > A[j]%2:
                A[i], A[j] = A[j], A[i]
            
            if A[i] %2 == 0: i += 1
            if A[j] %2 == 1: j -= 1

        return A
