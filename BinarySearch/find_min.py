"""This one was very confusing; I will revisit at a later date."""

def find_min(nums: list) -> int:
    left, right = 0, len(nums) - 1
    curr_min = float('inf')

    while left <= right:
        midpoint = (left + right) // 2
        curr_min = min(curr_min, nums[midpoint])

        if nums[midpoint] > nums[right]:
            left = midpoint + 1

        else:
            right = midpoint - 1

    return min(curr_min, nums[left])