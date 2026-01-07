from __future__ import annotations
from typing import List
from dataclasses import dataclass


@dataclass
class State:
    x_list: List[int]
    y_list: List[int]
    z_list: List[int]

    def expand(self, x: int, y: int, z: int, arr: List[int]) -> List[State]:
        length: int = len(arr)
        child_states: List[State] = []
        for subarray_length, allowed in enumerate([x, y, z], 1):
            left = allowed - self.get_used(subarray_length)
            if left <= 0:
                continue
            for i in range(len(arr) - subarray_length +1):
                if not self.conflicts(i, subarray_length, arr):
                    new_state: State = self.get_new_state(subarray_length, i)
                    child_states.append(new_state)
        return child_states
    
    def get_used(self, subarray_length: int) -> int:
        match subarray_length:
            case 1:
                return len(self.x_list)
            case 2:
                return len(self.y_list)
            case 3:
                return len(self.z_list)
        raise RuntimeError("Logic Probelem here")
    
    def get_new_state(self, subarray_length: int, start_pos: int):
        match subarray_length:
            case 1:
                new_xlist = self.x_list.copy()
                new_xlist.append(start_pos)
                new_state = State(new_xlist, self.y_list, self.z_list)
            case 2:
                new_ylist = self.y_list.copy()
                new_ylist.append(start_pos)
                new_state = State(self.x_list, new_ylist, self.z_list)
            case 3:
                new_zlist = self.z_list.copy()
                new_zlist.append(start_pos)
                new_state = State(self.x_list, self.y_list, new_zlist)
            case _:
                raise RuntimeError("Logic problem here.")
        return new_state
    
    def conflicts(self, pos: int, claiming_length: int, arr: List[int]) -> bool:
        for claimed_length, claimed_positions in enumerate([self.x_list, self.y_list, self.z_list], 1):
            for idx in claimed_positions:
                if idx + claimed_length -1 < pos:
                    continue
                elif pos + claiming_length -1 < idx:
                    continue
                return True
        return False
    
    def get_score(self, arr: List[int]):
        total = 0
        for length, start_positions in enumerate([self.x_list, self.y_list, self.z_list], 1):
            for pos in start_positions:
                total += sum(arr[idx] for idx in range(pos, pos+length))
        return total


def maxsubarray(arr: List[int], x: int, y: int, z: int) -> int:
    stack: List[State] = [State([],[],[])]
    bssf: int = 0
    while stack:
        state: State = stack.pop()
        child_states: List[State] = state.expand(x, y, z, arr)
        for child in child_states:
            score = child.get_score(arr)
            if score > bssf:
                bssf = score
            stack.append(child)
    return bssf

nums = [1, 2, 3]
x = 0
y = 0
z = 1
print(maxsubarray(nums, x, y, z))