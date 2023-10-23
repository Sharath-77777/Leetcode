class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # n:i  or  value: index     inverse of what we usually do

        for i, n in enumerate(nums): #retuns index, value
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n]=i
        return 