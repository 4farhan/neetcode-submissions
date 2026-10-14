class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for self in nums: 
            if self in hashset:
                    return True
            hashset.add(self)
        return False