# There are N dominoes in a line, and we place each domino vertically upright.

# In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



# After each second, each domino that is falling to the left pushes the adjacent domino on the left.

# Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

# When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

# For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

# Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

# Return a string representing the final state. 

# Example 1:

# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
# Example 2:

# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second domino.
# Note:

# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'




class Solution(object):
    def pushDominoes(self, d):
        """
        :type d: str
        :rtype: str
        """
        d = 'L' + d + 'R'
        res = []
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.': continue
            middle = j - i - 1
            if i: res.append(d[i])
            if d[i] == d[j]: res.append(d[i] * middle)
            elif d[i] == 'L' and d[j] == 'R': res.append('.' * middle)
            else: res.append('R' * (middle / 2) + '.' * (middle % 2) + 'L' * (middle / 2))
            i = j
        return ''.join(res)

# Intuition:
# Whether be pushed or not, depend on the shortest distance to 'L' and 'R'.
# Also the direction matters.