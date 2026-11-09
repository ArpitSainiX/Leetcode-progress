// LeetCode Solution: Fruit Into Baskets
// Submitted: 2026-11-09T15:05:41.450Z
// Language: Python3

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        start = 0
        max_len = 0
        f_count = defaultdict(int)

        for end in range(len(fruits)):
            f_count[fruits[end]] += 1
            while len(f_count) > 2:
                f_count[fruits[start]] -= 1
                if f_count[fruits[start]] == 0:
                    del f_count[fruits[start]]
                start += 1
            max_len = max(max_len, end-start+1)
        return max_len