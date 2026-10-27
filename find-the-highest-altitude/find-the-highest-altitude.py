// LeetCode Solution: Find The Highest Altitude
// Submitted: 2026-10-27T11:11:53.470Z
// Language: Python3

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = [0]
        curr_gain = 0

        for p in gain:
            curr_gain += p
            ans.append(curr_gain)
        return max(ans)
        # n = len(gain)
        # prefix_arr = [0]*n
        # prefix_arr[0] = gain[0]

        # for i in range(1, len(gain)):
        #     prefix_arr[i] = prefix_arr[i-1] + gain[i]

        # max_elem = max(prefix_arr)
        # if max_elem <= 0:
        #     return 0
        # return max_elem