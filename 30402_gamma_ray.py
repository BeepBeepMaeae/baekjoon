import sys

def solve():
    for _ in range(15):
        line = sys.stdin.readline().strip().split()
        for pixel in line:
            if pixel == 'w':
                print("chunbae")
                return
            elif pixel == 'b':
                print("nabi")
                return
            elif pixel == 'g':
                print("yeongcheol")
                return

solve()