class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1]*len(nums)
        pre = 1
        #prefix loop
        for i in range(len(nums)):
            
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(len(nums) -1,-1,-1):
            res[i] *= post
            post *= nums[i]
        return res

                
            



        #prefix * postfix loop