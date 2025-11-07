"""
Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target.

    Args:
        nums: List of integers
        target: Target sum

    Returns:
        List of two indices
    """
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    return []


if __name__ == "__main__":
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Two Sum Example:")
    print(f"Input: nums = {nums}, target = {target}")
    print(f"Output: {result}")
    print(
        f"Explanation: nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}"
    )
