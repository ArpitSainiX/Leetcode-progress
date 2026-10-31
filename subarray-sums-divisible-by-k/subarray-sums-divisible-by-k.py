// LeetCode Solution: Subarray Sums Divisible By K
// Submitted: 2026-10-31T13:55:55.643Z
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