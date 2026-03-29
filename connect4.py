#!/usr/bin/env python3
"""connect4 - Connect Four."""
import sys,argparse,json,random
def make_board():return [[" "]*7 for _ in range(6)]
def drop(b,col,p):
    for r in range(5,-1,-1):
        if b[r][col]==" ":b[r][col]=p;return r
    return -1
def check_win(b,p):
    for r in range(6):
        for c in range(7):
            for dr,dc in [(0,1),(1,0),(1,1),(1,-1)]:
                if all(0<=r+i*dr<6 and 0<=c+i*dc<7 and b[r+i*dr][c+i*dc]==p for i in range(4)):return True
    return False
def main():
    p=argparse.ArgumentParser(description="Connect Four")
    p.add_argument("--games",type=int,default=100)
    args=p.parse_args()
    stats={"R":0,"Y":0,"draw":0}
    for _ in range(args.games):
        b=make_board();turn="R"
        for move in range(42):
            cols=[c for c in range(7) if b[0][c]==" "]
            if not cols:stats["draw"]+=1;break
            col=random.choice(cols);drop(b,col,turn)
            if check_win(b,turn):stats[turn]+=1;break
            turn="Y" if turn=="R" else "R"
        else:stats["draw"]+=1
    print(json.dumps({"games":args.games,"results":stats}))
if __name__=="__main__":main()
