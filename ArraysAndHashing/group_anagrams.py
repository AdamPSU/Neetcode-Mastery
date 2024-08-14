"""
It turns out I don't know as much about dictionaries as I thought
I did. I should probably review dictionary methods/spend more time
with them before moving onto a new category.
"""

def group_anagrams_first(strs: list):
    """
    This solution is very inefficient, largely because of my
    lack of experience with dictionaries.

    - First for loop: first, I individually sort each string,
      not considering the idea of sorting within the later for
      loop.

    - Second for loop: then, forgetting about dict.get(), I
      attempt to validate each entry. Additionally, I create
      careless arrays to store values when it can all be done
      in-place.

    - Third for loop: I didn't know dict.values() could be
      converted to a list. Now I know for next time.

    - Space Complexity: O(N), for all the strings in strs
    """

    if len(strs) == 1:
        return [strs]

    arr = []
    for string in strs:
        string = str(sorted(string))
        arr.append(string)

    freq = {}

    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]].append(strs[i])
        else:
            freq[arr[i]] = [strs[i]]

    angrms = []

    for value in freq.values():
        angrms.append(value)

    return angrms


def group_anagrams_second(strs: list):
    """
    This solution attempts to do the previous, but
    far more efficient in terms of space complexity and
    lines of code.

    First, initialize a dict. Then, loop through all the strings
    in the strs list. Sort the string and let it be a key in the
    dictionary. If it isn't already a key, let it be an empty list.
    Otherwise, append the string into the dictionary
    """

    anagrams = {}

    for string in strs:
        sorted_str = ''.join(sorted(string))

        anagrams[sorted_str] = anagrams.get(sorted_str, [])
        anagrams[sorted_str].append(string)

    return list(anagrams.values())
