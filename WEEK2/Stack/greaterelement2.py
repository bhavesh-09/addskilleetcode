class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s=[]
        s.append(0)
        result=[-1]*len(nums)
        for i in range(1,len(nums)*2):
            i%=len(nums)
            while s and nums[i] > nums[s[-1]]:
                no=s.pop()
                result[no]=nums[i]
            s.append(i)
        return result
