def two_sum_first(nums: list, target: int):
    """
    This is an exhaustive approach (O(N^2)) that
    manages to solve two_sum without incurring
    more complexity.
    """

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def two_sum_second(nums: list, target: int):
    """
    This approach is more performant at the expense of increased space complexity.
    A hash map is initialized to keep track of num/idx pairs. Then, as we iterate
    through the nums list, we make note that to solve this problem, it suffices
    to find a value such that the target minus the current number is all that is
    needed.

    Example:
        nums = [1, 2, 3], target = 5

    For the first value (1), we can calculate the desired value as follows:
    5 - 1 = 4. We then check to see if this value is in our hash map; if it is,
    we've found our pair. If not, then we simply add the current number
    to the hashmap, along with its corresponding index.

    """

    prev = {}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in prev:
            return [prev[diff], i]

        prev[nums[i]] = i


