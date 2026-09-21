// LeetCode Solution: Group Anagrams
// Submitted: 2026-09-21T11:25:48.467Z
// Language: Python3

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        # for s in strs:
        #     groups["".join(sorted(s))].append(s)
        # return list(groups.values())

        for s in strs:
            key = "".join(sorted(s))
            groups[key].append(s)
        return list(groups.values())