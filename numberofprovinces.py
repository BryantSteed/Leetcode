from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        components = []
        for i in range(len(isConnected)):
            if i not in visited:
                component = self.explore(isConnected, visited, i)
                components.append(component)
        return len(components)

    def explore(self, isConnected: List[List[int]], visited, city):
        """LeetCode 547: Number of Provinces"""
        component = set([city])
        visited.add(city)
        connections = isConnected[city]
        for i, connected in enumerate(connections):
            if i not in visited and connected == 1:
                gained = self.explore(isConnected, visited, i)
                component = component.union(gained)
        return component
