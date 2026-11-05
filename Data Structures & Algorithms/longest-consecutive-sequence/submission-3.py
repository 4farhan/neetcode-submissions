from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)

        for num in s:
            if (num - 1) not in s:      # num is the start of a run
                length = 1
                while (num + length) in s:
                    length += 1
                longest = max(longest, length)

        return longest