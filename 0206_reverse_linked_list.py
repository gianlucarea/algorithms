# 206. Reverse Linked List
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        current = head
        prev = None
        while current:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        return prev
