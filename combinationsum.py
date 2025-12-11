from typing import List

class Solution:
    class State:
        def __init__(self, collection: List[int]):
            self.lst = collection
            self.sum = sum(collection)
            self.tup = tuple(sorted(collection))

        def __hash__(self):
            return hash(self.tup)
        
        def __eq__(self, other):
            return self.sum == other.sum
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """Leetcode 39. Combination Sum"""
        stack = [Solution.State([])]
        accepted = set()
        while stack:
            state = stack.pop()
            for candidate in candidates:
                if state.sum + candidate < target:
                    stack.append(Solution.State(state.lst + [candidate]))
                elif state.sum + candidate == target:
                    accepted.add(Solution.State(state.lst+ [candidate]))
        accepted_format = []
        for solution in accepted:
            accepted_format.append(solution.lst)
        return accepted_format