def valid_sudoku(board):
    """
    Determine if a 9x9 Sudoku board is valid.
    
    :param board: List[List[str]] - A 9x9 list representing the Sudoku board
    :return: bool - True if the board is valid, False otherwise
    """
    for i in range(9):
            set1 = set()
            set2 = set() 
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in set1:
                        return False
                    else:
                        set1.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in set2:
                        return False
                    else:
                        set2.add(board[j][i])
    for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                box_set = set()

                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):

                        if board[i][j] != '.':
                            if board[i][j] in box_set:
                                return False

                            box_set.add(board[i][j])
    return True

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]


print(valid_sudoku(board)) 