# 234. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        left , right = 0 , len(result)-1
        while left <= right:
            if result[left] != result[right]:
                return False
            left += 1
            right -= 1
        return True
