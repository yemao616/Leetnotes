# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next: # slow record the middle position, fast is the end/None node
            slow = slow.next
            fast = fast.next.next
        

        dummy = None  # reverse the second part from slow
        while slow:
            nxt = slow.next
            slow.next = dummy
            dummy = slow
            slow = nxt
        
        while dummy:  # compare 
            if dummy.val != head.val:
                return False
            dummy = dummy.next
            head = head.next
        return True
        