# Key takeaways: dict.get(key, 0) is a good and safe way to
# access a value in a dictionary. If a a value doesn't exist, it simply
# imputes a zero in its place. Additionally, many sorting algorithms
# run on O(1) complexity.


def is_anagram_first(s: str, t: str) -> bool:
    """
    While this solution is inefficient in terms of
    time complexity (O(nlog(n))), it is likely the only solution
    that is O(1) in space complexity.
    """

    return sorted(s) == sorted(t)


def is_anagram_second(s: str, t: str) -> bool:
    """
    This solution is O(n). It initializes two frequency
    maps and compares them. If any one of the counts do
    not match with the other counter, it is not an anagram,
    and False is returned.
    """

    if len(s) != len(t): return False

    s_freq, t_freq = {}, {}

    for char_idx in range(len(s)):
        s_freq[s[char_idx]] = s_freq.get(s[char_idx], 0) + 1
        t_freq[t[char_idx]] = t_freq.get(t[char_idx], 0) + 1

    return s_freq == t_freq


def is_anagram_third(s: str, t: str) -> bool:
    """
    This solution is quite clever. It achieves the same O(N)
    complexity as the previous solution, but it cuts down on
    space complexity by incrementing the t counter by -1.
    If the sum of all characters does not end up being zero,
    it is not a valid anagram, and False is returned.
    """

    if len(s) != len(t): return False

    counter = {}

    for i in range(len(s)):
        counter[s[i]] = counter.get(s[i], 0) + 1
        counter[t[i]] = counter.get(t[i], 0) - 1

    for char in counter:
        if counter[char] != 0:
            return False

    return True


