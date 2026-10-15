class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sorted_string = ''.join(sorted(s))
            groups[sorted_string].append(s)
            pass

        return list(groups.values())