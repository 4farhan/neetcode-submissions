class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = Counter(nums)
        result = sorted(d.items(), key=lambda pair: pair[1], reverse=True)
        return [result[0] for result in result[:k]]



