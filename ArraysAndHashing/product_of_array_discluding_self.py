"""
In-place operations cannot be done when subsequent
array entries depend on the entries in the original array.
"""

def product_except_self_first(nums: list) -> list:
    """
    O(N^2) solution that exhaustively calculates the
    product for each number in the array.
    """

    prods = []

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i == j:
                continue

            product *= nums[j]

        prods.append(product)

    return prods
