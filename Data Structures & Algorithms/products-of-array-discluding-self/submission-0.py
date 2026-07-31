class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_list = []
        pre = 1
        post = 1
        
        
        for i in range(len(nums)):
            if i == 0:
                prod_list.append(1)
            else:
                pre *= nums[i-1]
                prod_list.append(pre)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                continue
            else:
                post *= nums[i+1]
                prod_list[i] *= post

        return prod_list
