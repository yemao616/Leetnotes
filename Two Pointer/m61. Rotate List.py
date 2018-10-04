# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not k:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        n = 0
        while head:
            n += 1
            head = head.next
        k = k%n
        if k:
            left = right = dummy
            for _ in xrange(k):
                right = right.next

            while right and right.next:
                left = left.next
                right = right.next

            if left != dummy:
                old_head = dummy.next
                dummy.next = left.next
                right.next = old_head
                left.next = None
        return dummy.next



class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        
        old_head = head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        k = k%len(nodes)
        if k==0:
            return old_head
        
        new_head = nodes[-k]
        nodes[-1].next = old_head
        nodes[-k-1].next = None
        
        return new_head