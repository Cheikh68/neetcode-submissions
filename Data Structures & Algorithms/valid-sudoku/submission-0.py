from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        columns = defaultdict(list)
        squares = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val != ".":     
                    rows[r].append(val)
                    columns[c].append(val)

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                square_num = (row // 3) * 3 + (col // 3)
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] != ".":
                            squares[square_num].append(board[r][c])

        for row, numbers in rows.items():
            if len(numbers) != len(set(numbers)):
                return False
        
        for column, numbers in columns.items():
            if len(numbers) != len(set(numbers)):
                return False

        for square, numbers in squares.items():
            if len(numbers) != len(set(numbers)):
                return False

        return True
