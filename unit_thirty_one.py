#pop quiz 1 and 2
count = 0
def find_heaviest_coin(coins):
    global count 
    count += 1
    if len(coins) == 1:
        return coins[0]
    else:
        mid = len(coins)//2
        left = coins[:mid]
        right = coins[mid:]
        left_weight = sum([coin.get('weight') for coin in left])
        right_weight = sum([coin.get('weight') for coin in right])
        
        if left_weight > right_weight:
            return find_heaviest_coin(left)
        elif left_weight < right_weight:
            return find_heaviest_coin(right)
        else:
            return find_heaviest_coin(coins[len(coins)//2:])
coins = [
    
        {'coins' : 1 , 'weight': 1},
        {'coins' : 2 , 'weight': 2},
        {'coins' : 3 , 'weight': 3},
        {'coins' : 4 , 'weight': 4},
        {'coins' : 5 , 'weight': 5},
        {'coins' : 6 , 'weight': 6},
        {'coins' : 7 , 'weight': 7},
        {'coins' : 8 , 'weight': 8},
        #{'coins' : 9 , 'weight': 9}
    
]
       
        

coin = find_heaviest_coin(coins)
print(coin, " ", count)


#pair programming

def tromino_tiling(board, n, top_col, top_row, mis_col, mis_row):
    if n == 2:
        tile = 1
        for r in range(2):
            for c in range(2):
                if top_row + r != mis_row or top_col + c != mis_col:
                    board[top_row + r][top_col + c] = tile
        return 
    
    mid = n // 2
    center_row, center_col = top_row + mid, top_col + mid

    # Determine which quadrant the missing tile is in
    if mis_row < center_row and mis_col < center_col:
        quadrant = 1
    elif mis_row < center_row and mis_col >= center_col:
        quadrant = 2
    elif mis_row >= center_row and mis_col < center_col:
        quadrant = 3
    else:
        quadrant = 4

    # Place the tromino in the center of the 4 quadrants
    if quadrant != 1:
        board[center_row - 1][center_col - 1] = 1
    if quadrant != 2:
        board[center_row - 1][center_col] = 1
    if quadrant != 3:
        board[center_row][center_col - 1] = 1
    if quadrant != 4:
        board[center_row][center_col] = 1

    # Recursive calls for each quadrant
    if quadrant == 1:
        tromino_tiling(board, mid, top_col, top_row, mis_col, mis_row)
    else:
        tromino_tiling(board, mid, top_col, top_row, center_col - 1, center_row - 1)
    
    if quadrant == 2:
        tromino_tiling(board, mid, center_col, top_row, mis_col, mis_row)
    else:
        tromino_tiling(board, mid, center_col, top_row, center_col, center_row - 1)

    if quadrant == 3:
        tromino_tiling(board, mid, top_col, center_row, mis_col, mis_row)
    else:
        tromino_tiling(board, mid, top_col, center_row, center_col - 1, center_row)

    if quadrant == 4:
        tromino_tiling(board, mid, center_col, center_row, mis_col, mis_row)
    else:
        tromino_tiling(board, mid, center_col, center_row, center_col, center_row)

def print_board(board):
    for row in board:
        print(' '.join(str(col) for col in row))
    print()
    
def solve_tromino(n, mis_row, mis_col):
    board = [[0 for _ in range(n)] for _ in range(n)]
    tromino_tiling(board, n, 0, 0, mis_col, mis_row)
    print_board(board)

n = 8
mis_row, mis_col = 3, 5
solve_tromino(n, mis_row, mis_col)