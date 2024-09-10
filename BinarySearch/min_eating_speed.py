"""
I was able to solve this one completely on my own, but I took a little
long and I definitely got impatient while doing so. I need to tell myself
to stop spam-submitting until I fully understand where my program goes wrong.
"""

import math

def min_eating_speed(piles: list, h: int) -> int:
    left, right = 1, max(piles)
    res = float('inf')

    while left <= right:
        rate = (left + right) // 2
        max_hours = h

        for pile in piles:
            max_hours -= math.ceil(pile / rate)

        if max_hours < 0:
            left = rate + 1

        else:
            res = min(res, rate)
            right = rate - 1

    return res