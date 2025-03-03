#148 Sort List
#Given the head of a linked list, return the list after sorting it in ascending order.

class Solution(object):
# INSERTION SORT (O(n^2))
    def sortListWithInsertionSort(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = dummy = ListNode(0)
        while head:
            if cur and cur.val > head.val: # reset pointer only when new number is smaller than pointer value
                cur = dummy
            while cur.next and cur.next.val < head.val: # classic insertion sort to find position
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next # insert
        return dummy.next
    
# MERGE SORT (O(n logn))
    def sortListWithMergeSort(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # cut the list into two halves
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        
        return self.merge(l, r)
    
    def merge(self, l, r):
        if l is None:
            return r
        elif r is None:
            return l
        
        dummy = ListNode(0)
        head = dummy
        
        while l and r:
            if l.val <= r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next
            
        head.next = l if r is None else r
        return dummy.next