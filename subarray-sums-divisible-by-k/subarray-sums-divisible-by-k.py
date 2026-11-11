// LeetCode Solution: Subarray Sums Divisible By K
// Submitted: 2026-11-11T16:22:38.312Z
// Language: Python3

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0
        p_mod = 0
        freq = {0:1}

        for el in nums:
            p_mod = (p_mod + el) % k
            if p_mod in freq:
                count += freq[p_mod]
                freq[p_mod] += 1
            else:
                freq[p_mod] = 1
        return count