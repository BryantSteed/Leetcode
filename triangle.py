from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Leetcode 120: Triangle"""
        n = len(triangle)
        dp_triangle = []
        for i, row in enumerate(triangle):
            if i == 0:
                dp_triangle.append([row[0]])
                continue
            new_dp_row = []
            for j in range(len(row)):
                prev_index_case = dp_triangle[i-1][j-1] + row[j] if j > 0 else float("inf")
                same_index_case = dp_triangle[i-1][j] + row[j] if j < i else float("inf")
                taken = min(prev_index_case, same_index_case)
                new_dp_row.append(taken)
            dp_triangle.append(new_dp_row)
        return min(dp_triangle[n-1])