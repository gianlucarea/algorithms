# 1472. Design Browser History
# You have a browser of one tab where you start on the homepage and you can visit another url, 
# get back in the history number of steps or move forward in the history number of steps.
# 

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.current = ListNode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_page = ListNode(url)
        new_page.prev = self.current
        self.current.next = new_page
        self.current = new_page

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        temp = self.current
        while temp.prev != None and steps != 0:
            steps -= 1
            temp = temp.prev
        self.current = temp
        return temp.val

    def forward(self, steps):
        temp = self.current
        while temp.next != None and steps != 0:
            steps -= 1
            temp = temp.next
        self.current = temp
        return temp.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)