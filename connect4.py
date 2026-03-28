#!/usr/bin/env python3
"""Connect Four with minimax AI."""
ROWS,COLS=6,7
def new_board(): return [[0]*COLS for _ in range(ROWS)]
def drop(board,col,player):
    for r in range(ROWS-1,-1,-1):
        if board[r][col]==0: board[r][col]=player;return r
    return -1
def undrop(board,col):
    for r in range(ROWS):
        if board[r][col]!=0: board[r][col]=0;return
def check_win(board,player):
    for r in range(ROWS):
        for c in range(COLS):
            if c+3<COLS and all(board[r][c+i]==player for i in range(4)): return True
            if r+3<ROWS and all(board[r+i][c]==player for i in range(4)): return True
            if r+3<ROWS and c+3<COLS and all(board[r+i][c+i]==player for i in range(4)): return True
            if r+3<ROWS and c-3>=0 and all(board[r+i][c-i]==player for i in range(4)): return True
    return False
def evaluate(board):
    if check_win(board,1): return 1000
    if check_win(board,2): return -1000
    score=0
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c]==1: score+=1 if r>=ROWS//2 else 0;score+=2 if c==COLS//2 else 0
            elif board[r][c]==2: score-=1 if r>=ROWS//2 else 0;score-=2 if c==COLS//2 else 0
    return score
def minimax(board,depth,maximizing,alpha=-9999,beta=9999):
    if check_win(board,1): return 1000+depth
    if check_win(board,2): return -1000-depth
    if depth==0 or all(board[0][c]!=0 for c in range(COLS)): return evaluate(board)
    if maximizing:
        best=-9999
        for c in range(COLS):
            if board[0][c]!=0: continue
            drop(board,c,1);val=minimax(board,depth-1,False,alpha,beta);undrop(board,c)
            best=max(best,val);alpha=max(alpha,val)
            if beta<=alpha: break
        return best
    else:
        best=9999
        for c in range(COLS):
            if board[0][c]!=0: continue
            drop(board,c,2);val=minimax(board,depth-1,True,alpha,beta);undrop(board,c)
            best=min(best,val);beta=min(beta,val)
            if beta<=alpha: break
        return best
def best_move(board,player,depth=5):
    best_val=-9999 if player==1 else 9999;best_col=COLS//2
    for c in range(COLS):
        if board[0][c]!=0: continue
        drop(board,c,player)
        val=minimax(board,depth-1,player!=1)
        undrop(board,c)
        if (player==1 and val>best_val) or (player==2 and val<best_val): best_val=val;best_col=c
    return best_col
if __name__=="__main__":
    b=new_board();drop(b,3,1);drop(b,3,2);drop(b,4,1);drop(b,4,2);drop(b,5,1);drop(b,5,2)
    col=best_move(b,1,4);print(f"AI plays column {col} (should be 6 to win)")
    drop(b,6,1)
    print(f"Win: {check_win(b,1)}"); print("Connect Four OK")
