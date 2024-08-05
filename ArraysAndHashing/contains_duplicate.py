def has_duplicate(nums) -> bool:
    """
    This is a good solution; its complexity is O(2*N),
    which in any case, is a good thing. However, it's important
    to note that having to compute the lengths of both the
    hashset and the array is not needed and can be optimized.
    """
    hashset = set(nums)

    return not len(hashset) == len(nums)


def has_duplicate_optimal(nums) -> bool:
    """
    This solution saves having to compute the lengths for
    both of the data structures, making it O(1) time.
    """

    hashset = set()

    for i in nums:
        hashset.add(i)
        if i in hashset:
            return True

    return False
