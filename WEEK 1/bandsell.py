class Solution:
    def maxProfit(self, prices):
        if not  prices:
            return 0    #with no profit
        ans=0
        minimum=prices[0]
        
        
        for i in range(1,len(prices)):
            if prices[i]<minimum:                   #
                minimum=prices[i]
            else:
                ans=max(ans,prices[i]-minimum)
        return ans
s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([5,4,3,18,32]))

