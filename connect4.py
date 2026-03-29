#!/usr/bin/env python3
"""Connect Four game logic with win detection."""
import sys

class Connect4:
    def __init__(self, rows=6, cols=7):
        self.rows, self.cols = rows, cols
        self.board = [[0]*cols for _ in range(rows)]
        self.current = 1
        self.winner = None
        self.moves_made = 0
    def drop(self, col):
        if self.winner or col < 0 or col >= self.cols: return False
        for r in range(self.rows-1, -1, -1):
            if self.board[r][col] == 0:
                self.board[r][col] = self.current
                self.moves_made += 1
                if self._check_win(r, col):
                    self.winner = self.current
                self.current = 3 - self.current
                return True
        return False
    def _check_win(self, r, c):
        p = self.board[r][c]
        for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:
            count = 1
            for d in (1, -1):
                nr, nc = r+dr*d, c+dc*d
                while 0<=nr<self.rows and 0<=nc<self.cols and self.board[nr][nc]==p:
                    count += 1; nr += dr*d; nc += dc*d
            if count >= 4: return True
        return False
    def is_draw(self):
        return self.winner is None and self.moves_made == self.rows * self.cols
    def to_string(self):
        lines = []
        for row in self.board:
            lines.append(" ".join("." if c==0 else "X" if c==1 else "O" for c in row))
        lines.append(" ".join(str(i) for i in range(self.cols)))
        return chr(10).join(lines)

def test():
    g = Connect4()
    for col in [3, 3, 4, 4, 5, 5, 6]:
        g.drop(col)
    assert g.winner == 1  # horizontal win
    g2 = Connect4()
    for col in [0, 1, 0, 1, 0, 1, 0]:
        g2.drop(col)
    assert g2.winner == 1  # vertical win
    g3 = Connect4()
    moves = [0,1,1,2,2,3,2,3,3,0,3]
    for col in moves:
        g3.drop(col)
    assert g3.winner == 1  # diagonal win
    s = g.to_string()
    assert "X" in s
    print("  connect4: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("Connect Four game")
