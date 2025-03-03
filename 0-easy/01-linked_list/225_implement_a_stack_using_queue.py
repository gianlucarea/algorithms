#225. Implement Stack using Queues

# Implement a last-in-first-out (LIFO) stack using only two queues. 
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

from collections import deque

class MyStack(object):

    def __init__(self):
        self.q = deque() 

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self):
        """
        :rtype: int
        """
        value = self.pop()
        self.push(value)
        return value
        
    def empty(self):
        return len(self.q) == 0
