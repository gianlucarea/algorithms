# 707 Design Linked List

# Design your implementation of the double linked list.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        
        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
        
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        current = self.head
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        else:
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
            if current.next:
                current.next.prev = current
        
        self.size -= 1