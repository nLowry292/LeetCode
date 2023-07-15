class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def containsDuplicate(lst: List[str]) -> bool:
            seen = set()
            for str in lst:
                if str in seen:
                    return True
                
                if str != ".":
                    seen.add(str)
            return False
        
        def boxDuplicate(board: List[List[str]], row: int, col: int) -> bool:
            box = []
            for i in range(0,3):
                for j in range(0,3):
                    box.append(board[row+i][col+j])
            return containsDuplicate(box)

        for row in board:
            if containsDuplicate(row):
                return False

        col = ["."]*9
        for i in range(0,9):
            for j in range(0,9):
                col[j]=board[j][i]
            if containsDuplicate(col):
                return False

        for k in range(0,3):
            for l in range(0,3):
                if boxDuplicate(board, 3*k, 3*l):
                    return False
        
        return True
        

