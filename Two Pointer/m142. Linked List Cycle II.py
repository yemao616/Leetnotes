# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Note: Do not modify the linked list.

# Follow up:
# Can you solve it without using extra space?



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
                
        if not fast or not fast.next:
            return None
        
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow


# Alogrithm Description:
# Step 1: Determine whether there is a cycle

# 1.1) Using a slow pointer that move forward 1 step each time

# 1.2) Using a fast pointer that move forward 2 steps each time

# 1.3) If the slow pointer and fast pointer both point to the same location after several moving steps, there is a cycle;

# 1.4) Otherwise, if (fast->next == NULL || fast->next->next == NULL), there has no cycle.

# Step 2: If there is a cycle, return the entry location of the cycle

# 2.1) L1 is defined as the distance between the head point and entry point

# 2.2) L2 is defined as the distance between the entry point and the meeting point

# 2.3) C is defined as the length of the cycle

# 2.4) n is defined as the travel times of the fast pointer around the cycle When the first encounter of the slow pointer and the fast pointer

# According to the definition of L1, L2 and C, we can obtain:

# the total distance of the slow pointer traveled when encounter is L1 + L2

# the total distance of the fast pointer traveled when encounter is L1 + L2 + n * C

# Because the total distance the fast pointer traveled is twice as the slow pointer, Thus:

# 2 * (L1+L2) = L1 + L2 + n * C => L1 + L2 = n * C => L1 = (n - 1) C + (C - L2)*

# It can be concluded that the distance between the head location and entry location is equal to the distance between the meeting location and the entry location along the direction of forward movement.