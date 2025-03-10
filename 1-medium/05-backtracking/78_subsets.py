# 78. Subsets
# Given an integer array nums of unique elements,
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. 
# Return the solution in any order.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

#EASY SOLUTION
    def subsets_easy(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums: 
            res += [item+[num] for item in res]
        return res