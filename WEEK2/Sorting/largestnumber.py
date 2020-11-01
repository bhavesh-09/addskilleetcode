class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any (map(bool,nums)):
            return "0"
        nums=list(map(str,nums))
        if len(nums)<2:
            return "".join(nums)
        
        def comp(p1,p2):
            return int(nums[p1] + nums[p2])>int(nums[p2]+nums[p1])
        
        for p1 in range(len(nums)-1):
            p2=p1+1
            
            while p1<len(nums) and p2<len(nums):
                if comp(p1,p2):
                    pass
                else:
                    nums[p2], nums[p1]=nums[p1],nums[p2]
                p2+=1
        return "".join(nums)