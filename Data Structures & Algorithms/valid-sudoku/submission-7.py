class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rows -
        for i in range(9):
            row = set()
            for j in range(9):
                item = board[i][j]
                if item in row:
                    return False
                elif item != ".":
                    row.add(item)



        # Columns -
        for i in range(9):
            col = set()
            for j in range(9):
                item = board[j][i]
                if item in col:
                    return False
                elif item != ".":
                    col.add(item)





        # 3x3 Sub-Boxes
        starting_positions = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for i, j in starting_positions:
            box = set()
            for row in range (i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in box:
                        return False
                    elif item != ".":
                        box.add(item)

        if not False:
            return True


        
        