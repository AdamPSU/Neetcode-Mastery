"""
I managed to come up with a solution, but it was slow and not
optimal. Still, once I witnessed the 'optimal' solution, I figured
it wasn't too bad. I don't think I'll have much trouble with two pointers.
"""

def two_sum_first(numbers, target: int):
    # O(Nlog(n))
    l, r = 1, len(numbers) - 1

    for curr_idx, num in enumerate(numbers):
        curr_target = target - num
        l, r = curr_idx + 1, len(numbers) - 1

        while l <= r:
            midpoint = (l + r) // 2

            if numbers[midpoint] == curr_target:
                return [curr_idx + 1, midpoint + 1]

            elif numbers[midpoint] > curr_target:
                r = midpoint - 1

            elif numbers[midpoint] < curr_target:
                l = midpoint + 1


def two_sum_second(numbers, target):
    l, r = 0, len(numbers) - 1

    while l <= r:
        curr_sum = numbers[l] + numbers[r]

        if curr_sum == target:
            return [l+1, r+1]

        elif curr_sum  > target:
            r -= 1

        elif curr_sum < target:
            l += 1
