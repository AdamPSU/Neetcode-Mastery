"""
While it was a struggle at first, I came to understand a lot more
when I narrated my steps as I went. I did have one hiccup, which
resulted in my original answer being O(N^2*M), however, that was
fixed by inspection of the top python solution. I did ultimately come
to understand the solution, and I'm a little upset that I wasn't able to
generate it first-try. Oh well.
"""

def threeSum(nums: list) -> list:
    nums.sort()
    results = []

    for i in range(len(nums) - 1):
        # only one unique number is necessary to find that given pair

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            curr_sum = nums[left] + nums[right]

            if curr_sum > target:
                right -= 1

            elif curr_sum < target:
                left += 1

            else:
                result = [nums[i], nums[left], nums[right]]
                results.append(result)
                left += 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return results
