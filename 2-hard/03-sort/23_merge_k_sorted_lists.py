#23. Merge k Sorted Lists
#Y ou are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it
 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists: 
            return 
        if len(lists) == 1:
            return lists[0]
        
        merged = lists[0]
        for i in range(1,len(lists)):
            merged = self.merge(merged,lists[i])
        return merged

    def merge(self,left,right):
        dummy = temp = ListNode(None)
        while left != None and right != None:
            if(left.val <= right.val):
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        temp.next = left or right
        return dummy.next