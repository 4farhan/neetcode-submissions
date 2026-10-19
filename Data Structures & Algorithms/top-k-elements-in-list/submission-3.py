class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        d = Counter(nums)
        return [num for num, freq in d.most_common(k)]



