def print_board(board):
    for row in board:
        print("".join(board[row]))

def is_safe(board,row,col,n):

    i,j = row-1,col-1
    while:

def solve(board,row,col,n):

    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i,j =row-1,col+1




n=int(input("Enter a number: "))
board=[["." for i in range(n)]for i in range(n)]
solve(board,0,n)
