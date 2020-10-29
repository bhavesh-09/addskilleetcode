class Solution:
    def search(self, nums, target):
        l=0
        h=len(nums)-1
        if not nums:
            return -1
        while l<=h:
            mid=(l+h)//2
            if target==nums[mid]:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    h=mid-1
                else:
                    l=mid+1 
            else:
                if nums[mid]<=target<=nums[h]:
                    l=mid+1
                else:
                    h=mid-1
        return -1

s=Solution()
print(s.search( [4,5,6,7,0,1,2], target = 0))