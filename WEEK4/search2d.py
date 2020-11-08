class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        
        row=0 
        for i in range(len(matrix)):
                if target==matrix[i][0] or target==matrix[i][-1]:
                    return True 
                elif target > matrix[i][0] and target < matrix[i][-1] :
                    row=i 
                    break
                    
        l,i=0,len(matrix[row]) - 1
        while l<=i:
            mid=l+(i-l)//2
            if target == matrix[row][mid]:
                return True 
            elif target > matrix[row][mid]:
                l=mid+1
            else:
                i=mid-1
        return False 
        