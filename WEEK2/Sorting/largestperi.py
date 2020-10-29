class Solution:
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        for i,j,k in zip(A,A[1:],A[2:]):
            if j+k>i:
                return i+j+k
        return 0 

s=Solution()
print(s.largestPerimeter( [4,9,2,3]))