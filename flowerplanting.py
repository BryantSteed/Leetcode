from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        """LeetCode 1042. Flower Planting With No Adjacent"""
        adj = {i : [] for i in range(1,n+1)}
        for path in paths:
            adj[path[0]].append(path[1])
            adj[path[1]].append(path[0])
        colors = [1,2,3,4]
        color_assignments = []
        for node in range(1, n+1):
            if node == 1:
                color_assignments.append(1)
                continue
            for color in colors:
                if Solution.is_unique(adj[node], color, color_assignments):
                    color_assignments.append(color)
                    break
        return color_assignments
    
    def is_unique(neighbors, color, color_assignments):
        for neighbor in neighbors:
            if len(color_assignments) < neighbor:
                continue
            if color_assignments[neighbor-1] == color:
                return False
        return True
