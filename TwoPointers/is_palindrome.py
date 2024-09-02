"""
This problem was not too hard (it is a leetcode easy),
but I found it quite annoying that some of the top solutions
are so confusing. The concept of two-pointers doesn't seem
to bad, at least from a glance.
"""

def is_palindrome(s: str) -> bool:
    """
    O(n/2) solution using two pointers.
    """
    l, r = 0, len(s) - 1 # left and right pointers

    while l < r:
        if not s[l].isalnum():
            # left is not alphanumeric, delete
            l += 1
            continue
        elif not s[r].isalnum():
            # right is not alphanumeric, delete
            r -= 1
            continue

        if s[l].lower() != s[r].lower():
            # if any two characters are not equivalent, it is not a palindrome
            return False

        l += 1
        r -= 1

    return True