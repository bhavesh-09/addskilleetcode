class Solution:
    def majorityElement(self, nums):
        nums.sort()
        print(nums)
        return nums[len(nums)//3]






s=Solution()
print(s.majorityElement([1,4,4,4,2,4]))
