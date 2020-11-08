class Solution:
    def isValidSudoku(self, board) :
        row=[set() for i in range(9)]
        col=[set() for i in range(9)]
        boxes=[set() for i in range(9)]
        
        for j in range(9):
            for k in range(9):
                num=board[j][k]
                if num==".":
                    continue
                
                if num in row[j] or num in col[k]or num in boxes[(j//3)*3+k//3]:
                    return False
                
                row[j].add(num)
                col[k].add(num)
                boxes[(j//3)*3+k//3].add(num)
        return True 


