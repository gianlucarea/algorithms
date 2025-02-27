#206. Reverse Linked List
#Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return

        current = head
        previous = None

        while current != None:
            temp = current.next 
            current.next = previous 
            previous = current 
            current = temp 

        return previous   