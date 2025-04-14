# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.
from collections import Counter
from typing import List
import unittest

# This solution finds the top k frequent elements using Counter and most_common(). 
# Time: O(n log n) (worst case), Space: O(n). Simple and Pythonic.
def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequent_table = Counter(nums)
    print(frequent_table.most_common())
    ans_table = frequent_table.most_common()
    ans = []
    for key,_ in ans_table:
        if k <= 0:
            break
        k -= 1
        ans.append(key)
    return ans


class TestMyFunctions(unittest.TestCase):
    def test_topKFrequent1(self):
        self.assertEqual(topKFrequent([1,1,1,2,2,3],2), [1,2])
    def test_topKFrequent2(self):
        self.assertEqual(topKFrequent([1],1), [1])

if __name__ == '__main__':
    unittest.main()