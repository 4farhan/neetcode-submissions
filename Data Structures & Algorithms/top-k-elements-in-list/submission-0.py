class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create a dDefaultDict, ictonary that has has the keys as nubers and the freq as values, return the array of the keys with 2 highest values? 
        d = Counter(nums)
        result = sorted(d.items(), key=lambda pair: pair[1], reverse=True)
        return [result[0] for result in result[:k]]



