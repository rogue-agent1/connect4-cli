#!/usr/bin/env python3
"""Connect Four with minimax AI."""
import sys
ROWS,COLS=6,7
def new_board(): return [[' ']*COLS for _ in range(ROWS)]
def display(b):
    for r in b: print('|'+'|'.join(r)+'|')
    print('+'+'+'.join(['-']*COLS)+'+')
    print(' '+''.join(str(i) for i in range(COLS)))
def drop(b,col,piece):
    for r in range(ROWS-1,-1,-1):
        if b[r][col]==' ': b[r][col]=piece; return r
    return -1
def undrop(b,col):
    for r in range(ROWS):
        if b[r][col]!=' ': b[r][col]=' '; return
def check_win(b,piece):
    for r in range(ROWS):
        for c in range(COLS):
            for dr,dc in [(0,1),(1,0),(1,1),(1,-1)]:
                if all(0<=r+i*dr<ROWS and 0<=c+i*dc<COLS and b[r+i*dr][c+i*dc]==piece for i in range(4)):
                    return True
    return False
def minimax(b,depth,alpha,beta,maximizing):
    if check_win(b,'O'): return 100+depth,None
    if check_win(b,'X'): return -100-depth,None
    if depth==0 or all(b[0][c]!=' ' for c in range(COLS)): return 0,None
    if maximizing:
        best=-999; best_c=COLS//2
        for c in range(COLS):
            if b[0][c]!=' ': continue
            drop(b,c,'O'); v,_=minimax(b,depth-1,alpha,beta,False); undrop(b,c)
            if v>best: best=v; best_c=c
            alpha=max(alpha,v)
            if alpha>=beta: break
        return best,best_c
    else:
        best=999; best_c=COLS//2
        for c in range(COLS):
            if b[0][c]!=' ': continue
            drop(b,c,'X'); v,_=minimax(b,depth-1,alpha,beta,True); undrop(b,c)
            if v<best: best=v; best_c=c
            beta=min(beta,v)
            if alpha>=beta: break
        return best,best_c
b=new_board()
# Demo game
for move in [3,3,4,2,5]:
    drop(b,move,'X'); _,ai_col=minimax(b,6,-999,999,True)
    if ai_col is not None: drop(b,ai_col,'O')
display(b)
