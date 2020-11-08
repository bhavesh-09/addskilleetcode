class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri=0
        connect=0
        rows=len(grid)
        columns=len(grid[0])
        
        for x in range(0,rows):
            for y in range(0,columns):
                
                if grid[x][y]==1:
                    peri += 4
                    
                    if x!=0 and grid[x-1][y]==1:
                        connect+=1
                        
                    if y!=0 and grid[x][y-1]==1:
                        connect+=1
                    
        return peri-(connect*2) 


