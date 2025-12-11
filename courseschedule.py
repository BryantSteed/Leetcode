from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """LeetCode 207. Course Schedule"""
        graph = {i : [] for i in range(numCourses)}
        for prereq in prerequisites:
            if prereq[0] == prereq[1]:
                return False
            graph[prereq[0]].append(prereq[1])
        pre_post = {i : [] for i in range(numCourses)}
        Solution.dfs(graph, pre_post)
        for u in graph:
            for v in graph[u]:
                u_pre = pre_post[u][0]
                u_post = pre_post[u][1]
                v_pre = pre_post[v][0]
                v_post = pre_post[v][1]
                if v_pre < u_pre and u_post < v_post:
                    return False
        return True
    
    def dfs(graph, prepost):
        num = 0
        visited = set()
        for node in graph:
            if node not in visited:
                num = Solution.explore(graph, prepost, node, num, visited)
    
    def explore(graph, prepost, node, num, visited):
        visited.add(node)
        prepost[node].append(num)
        num += 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                num = Solution.explore(graph, prepost, neighbor, num, visited)
        prepost[node].append(num)
        num += 1
        return num
