class Solution:
    def twoSum(self, nums ,t):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==t:
                    return i,j
s=Solution()
print(s.twoSum([2,9,11,15],7))
