from __future__ import annotations
from typing import AnyStr

def generate_all_subsequences(sequence: list[any])-> None :
    create_state_space_tree(sequence, [], 0)

def create_state_space_tree(
        sequence:list[any], current_subsequence: list[any], index: int
) -> None:
    if index == len(sequence):
        print(current_subsequence)
        return
    
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index+ 1)
    current_subsequence.pop()

if __name__ == "__main__":
    seq: list[any] = [3, 1, 2, 4]
    generate_all_subsequences(seq)

    seq.clear()
    seq.extend(["A", "B", "C"])
    generate_all_subsequences(seq)