#!/usr/bin/env python3
"""Terminal Connect Four game."""
import sys, random

ROWS, COLS = 6, 7
EMPTY, P1, P2 = '.', '🔴', '🟡'

def new_board(): return [[EMPTY]*COLS for _ in range(ROWS)]

def show(board):
    print('\n ' + ' '.join(str(i+1) for i in range(COLS)))
    for row in board: print('|' + '|'.join(row) + '|')
    print('+' + '-+'*COLS)

def drop(board, col, piece):
    for r in range(ROWS-1, -1, -1):
        if board[r][col] == EMPTY: board[r][col] = piece; return r
    return -1

def check_win(board, piece):
    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:
                if all(0<=r+i*dr<ROWS and 0<=c+i*dc<COLS and board[r+i*dr][c+i*dc]==piece for i in range(4)):
                    return True
    return False

def ai_move(board, piece):
    opp = P1 if piece == P2 else P2
    for p in [piece, opp]:
        for c in range(COLS):
            b = [row[:] for row in board]
            if drop(b, c, p) >= 0 and check_win(b, p): return c
    valid = [c for c in range(COLS) if board[0][c] == EMPTY]
    return random.choice(valid) if valid else 0

def play():
    board = new_board()
    show(board)
    for turn in range(ROWS * COLS):
        piece = P1 if turn % 2 == 0 else P2
        if piece == P1:
            while True:
                try: col = int(input(f"\n{piece} Column (1-7): ")) - 1
                except: continue
                if 0 <= col < COLS and board[0][col] == EMPTY: break
        else:
            col = ai_move(board, P2)
            print(f"\n{piece} plays column {col+1}")
        drop(board, col, piece)
        show(board)
        if check_win(board, piece):
            print(f"\n{'You win! 🎉' if piece == P1 else 'AI wins! 🤖'}"); return
    print("\nDraw!")

if __name__ == '__main__':
    play()
