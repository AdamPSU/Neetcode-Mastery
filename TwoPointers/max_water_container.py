"""
This time, I was able to converge to a solution in about
35 minutes. It took a little long, but I was proud because I was
able to truly say I did it on my own. It truly does suck not being
able to narrate the thought process live.

My approach was simple: I reasoned that you only ever needed to move
the smallest pointer, or the pointer with the smallest height, and it
was easy sailing from there. Just calculate the area of that new pointer,
and compare it with the current max area.

Time comp: O(N)
Space comp: O(1)
"""

def maxArea(heights) -> int:
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        length = right - left

        if heights[left] <= heights[right]:
            height = heights[left]
            left += 1

        else:
            height = heights[right]
            right -= 1

        area = length * height
        max_area = max(max_area, area)

    return max_area
