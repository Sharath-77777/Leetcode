class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ha = set()
        
        for i in nums:
            if(i in ha):
                return True
            ha.add(i)
        return False