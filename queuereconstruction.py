from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """Leetcode 406. Queue Reconstruction by Height"""
        n_people = len(people)
        s_people = people.copy()
        s_people.sort(key= lambda x: (x[0], -x[1]))
        new_people = [None for i in range(n_people)]
        placed = set()
        for person in s_people:
            height = person[0]
            in_front = person[1]
            constraint = in_front
            satisfied = 0
            for i in range(n_people):
                if constraint == satisfied and new_people[i] is None:
                    new_people[i] = person
                    break
                if new_people[i] is None:
                    satisfied += 1
                elif new_people[i][0] >= height:
                    satisfied += 1
        return new_people