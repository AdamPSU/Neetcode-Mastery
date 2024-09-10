"""
Very easy.
"""

def search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if nums[midpoint] < target:
            left = midpoint + 1

        elif nums[midpoint] > target:
            right = midpoint - 1

        else:
            return midpoint

    return -1