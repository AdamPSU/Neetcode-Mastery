# Once again, I struggle with the language syntax. Had I known how to
# sort a dictionary, this would not be a problem.

def top_k_frequent(nums: list, k: int):
    """
    Initialize a frequency map. Sort the dictionary
    by value, in descending order. Then, subset only
    the first k elements.

    Because this involves sorting, the fastest time
    achievable is O(Nlog(N)), with a space of O(N).
    """

    counter = {}

    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    counter = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
    return list(counter.keys())[:k]






