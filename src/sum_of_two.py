"""
Given a sorted array of numbers and a target number,
find a pair which sum is equal to target and return tuple of their position in array.

If no such pair return tuple of zeros.
"""
from typing import List, Tuple


def sum_of_two(array: List[int], target: int) -> Tuple[int, int]:
    """Implement me!"""
    raise NotImplementedError


def main():
    cases = (
        ([1, 3, 6, 6, 7, 9], 12, (2, 3)),
        ([6, 10, 46, 88, 91, 172], 101, (1, 4)),
        ([5, 6, 11, 25, 75, 91], 12, (0, 0)),
        ([2, 4, 11, 15, 42, 89], 11, (0, 0)),
        ([], 10, (0, 0)),
        ([1], 5, (0, 0)),
        ([1, 3], 4, (0, 1))
    )

    for array, target, expected in cases:
        output = sum_of_two(array, target)
        assert output == expected, f"Input: {array} {target} Output: {output} Expected: {expected}"

    print("All tests passed!")


if __name__ == '__main__':
    main()
