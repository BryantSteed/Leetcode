from typing import List, Dict, Tuple, Set

def lowest_operations(array: List[int], costs: List[int]) -> int:
    equalities: List[List[int]] = get_equalities(array)
    best_cost = best(equalities, costs,  array)
    return best_cost

def best(equalities: List[List[int]], costs: List[int], array: List[int]) -> int:
    array_tuple = tuple(array)
    if not hasattr(best, "memo"):
        best.memo = {}
    if not equalities:
        best.memo[array_tuple] = 0
        return 0
    if array_tuple in best.memo:
        return best.memo[array_tuple]
    curr_best = float('inf')
    for equality in equalities:
        for i in equality:
            test_array = array.copy()
            test_cost = costs[i]
            test_array[i] = test_array[i] + 1
            test_equalities = get_equalities(test_array)
            candidate_best = test_cost + best(test_equalities, costs, test_array)
            if candidate_best < curr_best:
                curr_best = candidate_best
    best.memo[array_tuple] = curr_best
    return curr_best


def get_equalities(array: List[int]):
    counts: Dict[int, int] = {}
    indexes: Dict[int, List[int]] = {}
    multiples: Set[int] = set()
    for i, num in enumerate(array):
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > 1:
            multiples.add(num)
        if num in indexes:
            indexes[num].append(i)
        else:
            indexes[num] = [i]
    equalities = []
    for multiple in multiples:
        equalities.append(indexes[multiple])
    return equalities

test = [1, 1, 1, 1, 1, 1, 1, 1]
costs = [1, 2, 3, 4, 5, 6, 7, 8]
print(lowest_operations(test, costs))