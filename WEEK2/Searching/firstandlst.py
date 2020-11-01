class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_position():
            l=0
            h=len(nums)-1
            while(l<=h):
                mid=(l+h)//2
                if nums[mid]>target:
                    h=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    h=mid-1
            if l<len(nums) and nums[l]==target:
                return l 
            else:
                return -1
        def last_position():
            l=0
            h=len(nums)-1
            r=-1
            while(l<=h):
                mid=(l+h)//2
                if nums[mid]>target:
                    h=mid-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    l=mid+1
            if h>=0 and nums[h]==target:
                return h
            else:
                return -1
        if not nums:
            return[-1,-1]
        return[first_position(),last_position()]