class Solution:
    def productExceptSelf(self,nums):
        length=len(nums)
        sol=[1]*length
        pre=1
        post=1
        for i in range(length):
            sol[i]*=pre
            pre*=nums[i]
            sol[length-i-1]*=post
            post*=nums[length-i-1]
        return(sol)    

ab=Solution()
res=ab.productExceptSelf([1,3,5,7,1])
print(res)
