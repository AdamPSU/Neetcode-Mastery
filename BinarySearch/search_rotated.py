"""
This problem was hard, but it taught a pretty important lesson.
Whenever there are multiple clauses in an if statement, instead of
being mad that I can't figure them all out at once, I should probably treat
them all individually, as with Neetcode's solution to this. That way, I understand
that they are all evaluating to the same thing. I will revisit this problem on a later
date.
"""

def search(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    # nums = [3,4,5,6,1,2], target = 1
    while left <= right:
        midpoint = (left + right) // 2

        if target == nums[midpoint]:
            return midpoint

        if nums[left] <= nums[midpoint]:
            if target > nums[midpoint] or target < nums[left]:
                # target < nums[left] = on the right side of midpoint
                left = midpoint + 1

            else:
                right = midpoint - 1

        else:
            if target < nums[midpoint] or target > nums[right]:
                right = midpoint - 1

            else:
                left = midpoint + 1

    return -1