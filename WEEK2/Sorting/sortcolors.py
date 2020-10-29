class Solution:
    def sortColors(self, nums):
        le=0
        current=0
        ri=len(nums)-1
        
        while current<=ri:
            if nums[current]==0:
                nums[le],nums[current]=nums[current],nums[le]
                le+=1
                current+=1
                
            elif nums[current]==2:
                nums[current],nums[ri]=nums[ri],nums[current]
                ri-=1
            else:
                current+=1
s=Solution()
print(s.sortColors([2,0,1])