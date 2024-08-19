"""
Instead of making a dictionary with unneeded values,
it suffices to just make a set of the numbers. Make sure
to avoid infinite while loops; properly check that values
increment.
"""

def longest_consecutive(nums) -> int:
    # Make a hashset to store the unique numbers
    hashset = set(nums)

    max_len = 0
    for n in hashset:
        # Copy the number
        k = n
        curr_len = 1


        while k + 1 in hashset:
            k += 1
            curr_len += 1

        if curr_len > max_len:
            max_len = curr_len

    return max_len

