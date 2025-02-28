#1700. Number of Students Unable to Eat Lunch

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        queue = collections.deque(students)
        i, counter = 0,0
        while queue:
            curr = queue.popleft()
            if(curr != sandwiches[i]):
                counter += 1
                queue.append(curr)
            else:
                i += 1
                counter = 0
            if counter == len(queue): break
        
        return len(queue)

        