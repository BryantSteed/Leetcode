from typing import List

class Solution:

    class Edge:
        def __init__(self, from_point: List[int], to_point: List[int]):
            self.weight = abs(from_point[0] - to_point[0]) + abs(from_point[1] - to_point[1])
            self.from_point = from_point
            self.to_point = to_point

    class Mst:
        def __init__(self, points: List[List[int]]):
            self.parents = {}
            for point in points:
                parent_point = tuple(point)
                self.parents[parent_point] = parent_point
        
        def find(self, point: List[int]):
            curr_point = tuple(point)
            curr_parent = self.parents[curr_point]
            while True:
                if curr_parent == curr_point:
                    return curr_parent
                curr_point = curr_parent
                curr_parent = self.parents[curr_point]
        
        def union(self, u: List[int], v: List[int]):
            u_parent = self.find(u)
            v_parent = self.find(v)
            if u_parent != v_parent:
                self.parents[u_parent] = v_parent

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Leetcode 1584. Min Cost to Connect All Points"""
        mst = Solution.Mst(points)
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                edges.append(Solution.Edge(points[i], points[j]))
        edges.sort(key=lambda x: x.weight)
        cost = 0
        for edge in edges:
            if mst.find(edge.from_point) == mst.find(edge.to_point):
                continue
            cost += edge.weight
            mst.union(edge.from_point, edge.to_point)
        return cost