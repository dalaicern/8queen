def is_safe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False


    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, ro, col, solutions):

    if col >= len(board):
        solutions.append([''.join('Q' if x else '.' for x in row) for row in board])
        return
    
    if col == 0:
        if is_safe(board, ro, col):

                board[ro][col] = 1

                solve_n_queens_util(board, ro, col + 1, solutions)

                board[ro][col] = 0

    else:
        for i in range(len(board)):
            if is_safe(board, i, col):

                board[i][col] = 1

                solve_n_queens_util(board, i, col + 1, solutions)

                board[i][col] = 0
    


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    row = int(input("input starting row (1 - 8): "))

    solve_n_queens_util(board, row - 1,  0, solutions)
    return solutions



all_solutions = solve_n_queens(8)

for index, solution in enumerate(all_solutions):
    print(f"Solution {index + 1}:")
    for row in solution:
        print(row)
    print()
