class Solution:
    def searchInsert(self, nums, target):
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)// 2
            if nums[m]==target:
                return m
            if target<nums[m]:
                r=m-1
            else:
                l=m+1
                 
        return l
s=Solution()
print(s.searchInsert([1,3,5,6],target=5))