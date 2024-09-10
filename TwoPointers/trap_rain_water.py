"""
The solution is straightforward, but it was pretty complicated
to come up with. I did not solve it myself, but my solution
was almost there. This was a good problem.
"""

def trap(height) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    res = 0

    while left < right:
        if left_max <= right_max:
            trapped_water = left_max - height[left]
            trapped_water = 0 if trapped_water < 0 else trapped_water

            left += 1
            left_max = max(left_max, height[left])
        else:
            trapped_water = right_max - height[right]
            trapped_water = 0 if trapped_water < 0 else trapped_water

            right -= 1
            right_max = max(right_max, height[right])

        res += trapped_water

    return res