class Solution:
    """This is a depth-first exhaustive search solution to the perfect squares problem.
    This implementation sucks because it explores way too many states."""

    class State:
        def __init__(self, count, total):
            self.count = count
            self.total = total

    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, n+1):
            squared = i**2
            if squared > n:
                break 
            squares.append(squared)
        bssf = float("inf")
        stack = [Solution.State(0, 0)]
        while stack:
            state = stack.pop()
            child_states = []
            for num in squares:
                new_total = num + state.total
                if new_total > n:
                    break
                new_count = state.count + 1
                child_states.append(Solution.State(new_count, new_total))
            for child in child_states:
                if child.count >= bssf:
                    continue
                if child.total == n:
                    bssf = child.count
                else:
                    stack.append(child)
        return bssf

class Solution:
    """This solution solves it way better with dynamic programming.
    It reduces the problem to a knapsack type problem where we are trying to minimize"""

    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(1, n+1):
            squared = i**2
            if squared > n:
                break 
            squares.append(squared)
        dp = [0]
        for i in range(1,n+1):
            min_cost = float("inf")
            for square in squares:
                if square > i:
                    break
                possibility = dp[i - square] + 1
                if possibility < min_cost:
                    min_cost = possibility
            dp.append(min_cost)
        return dp[-1]