// LeetCode Solution: Group Anagrams
// Submitted: 2026-09-21T11:24:43.492Z
// Language: Python3

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for s in strs:
            groups["".join(sorted(s))].append(s)
        return list(groups.values())