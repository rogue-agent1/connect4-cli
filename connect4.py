import argparse, random

ROWS, COLS = 6, 7

def make_board(): return [[" "]*COLS for _ in range(ROWS)]

def display(b):
    for r in b: print("|" + "|".join(r) + "|")
    print("+" + "+".join("-"*COLS) + "+")
    print(" " + " ".join(str(i) for i in range(COLS)))

def drop(b, col, piece):
    for r in range(ROWS-1, -1, -1):
        if b[r][col] == " ": b[r][col] = piece; return r
    return -1

def check_win(b, piece):
    for r in range(ROWS):
        for c in range(COLS):
            for dr, dc in [(0,1),(1,0),(1,1),(1,-1)]:
                if all(0<=r+dr*i<ROWS and 0<=c+dc*i<COLS and b[r+dr*i][c+dc*i]==piece for i in range(4)):
                    return True
    return False

def ai_move(b):
    for c in range(COLS):
        if b[0][c] != " ": continue
        r = drop(b, c, "O")
        if check_win(b, "O"): b[r][c] = " "; return c
        b[r][c] = " "
    for c in range(COLS):
        if b[0][c] != " ": continue
        r = drop(b, c, "X")
        if check_win(b, "X"): b[r][c] = " "; return c
        b[r][c] = " "
    center = [c for c in [3,2,4,1,5,0,6] if b[0][c] == " "]
    return center[0] if center else 0

def main():
    p = argparse.ArgumentParser(description="Connect Four")
    p.add_argument("--ai", action="store_true", help="Play vs AI")
    args = p.parse_args()
    b = make_board()
    turn = "X"
    while True:
        display(b)
        if check_win(b, "X"): print("X wins!"); break
        if check_win(b, "O"): print("O wins!"); break
        if all(b[0][c] != " " for c in range(COLS)): print("Draw!"); break
        if args.ai and turn == "O":
            col = ai_move(b)
            print(f"AI plays column {col}")
        else:
            try: col = int(input(f"{turn}'s turn (0-6): "))
            except (ValueError, EOFError): break
        if 0 <= col < COLS and b[0][col] == " ":
            drop(b, col, turn)
            turn = "O" if turn == "X" else "X"

if __name__ == "__main__":
    main()
