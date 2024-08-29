"""
I found out that there is a more efficient solution that the one
I came up with, however, it is quite an unbelievable  method. I don't know
how I can come up with a solution like that on the spot. Nevertheless,
I think I'm improving at not messing up the naive solution, which is a good
start.
"""

def dailyTemperatures(temperatures):
    """O(m*n) solution"""

    result = []

    for i in range(len(temperatures)):
        j = i
        counter = 0

        while j < len(temperatures) and temperatures[j] <= temperatures[i]:
            counter += 1
            j += 1
        else:
            if j >= len(temperatures):
                result.append(0)
            else:
                result.append(counter)

    return result