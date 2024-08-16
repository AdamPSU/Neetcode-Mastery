"""
This problem was HELL. I certainly learned new things, though.
For some reason, I thought that you could change the incrementor
on for loops. While I don't necessarily understand the optimal
answer, I will make sure to revisit this problem in the future.
"""

def encode(strs: list) -> str:
    res = ""

    for word in strs:
        res += str(len(word)) + "#" + word

    return res

def decode(s: str) -> list:
    res, i = [], 0

    while i < len(s):
        j = i

        while s[j] != '#':
            j += 1

        length = int(s[i:j]) # Takes into account double-digit integers
        res.append(s[j + 1: j + 1 + length])

        i = j + 1 + length

    return res






