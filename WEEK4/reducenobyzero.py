class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = 0
        while num > 0:
            result += 1
            if (num % 2 )==0 :
                num = num/2 
            else:
                num-=1
        return result   

#Approach 2 Bit 
class Solution:
    def numberOfSteps (self, num: int) -> int:
        result = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            result += 1
        return result