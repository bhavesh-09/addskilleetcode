class Solution:
    def  removeDuplicates(self,nums):
        N=len(nums)
        if N<=1:return N 
            
        i=j=1
        while i<N:
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1
            i+=1
        
        return j
        
s=Solution()
print(s.removeDuplicates([1,1,2]))





